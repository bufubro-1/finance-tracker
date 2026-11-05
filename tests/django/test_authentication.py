"""TASK-025A: P1-02 and scoped TC-053/055 authentication/session scenarios."""

import json
import pytest


AUTH_SETUP = r'''
import re
import secrets
import socket
def reject(*args, **kwargs):
    raise AssertionError("Unexpected external call")
socket.socket.connect = reject
import django
django.setup()
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.test import Client
from django.test.utils import setup_test_environment
setup_test_environment()
password = secrets.token_urlsafe(24)
user = get_user_model().objects.create_user("sample@example.invalid", password)
client = Client(HTTP_HOST="127.0.0.1", enforce_csrf_checks=True)
def csrf(client, path="/login/"):
    page = client.get(path)
    assert page.status_code == 200
    return re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', page.content.decode())[1]
def login(client, **overrides):
    data = {"username": user.email, "password": password, "csrfmiddlewaretoken": csrf(client)}
    data.update(overrides)
    return client.post("/login/", data)
'''


def test_login_logout_session_rotation_and_cookie_replay(run_django, migrated_prototype):
    run_django(AUTH_SETUP + r'''
session = client.session
session["synthetic_marker"] = True
session.save()
old_key = session.session_key
response = login(client, username="  SAMPLE@Example.INVALID  ")
assert response.status_code == 302 and response.url == "/"
cookie = client.cookies[settings.SESSION_COOKIE_NAME]
assert cookie.value != old_key and not Session.objects.filter(session_key=old_key).exists()
assert cookie["httponly"] and cookie["samesite"] == "Lax"
assert client.session["synthetic_marker"] is True
authenticated_cookie = cookie.value
for path in ("/", "/accounts/"):
    response = client.get(path)
    assert response.status_code == 200
    assert "no-store" in response["Cache-Control"]
    assert "Çıkış yap".encode() in response.content
assert client.get("/logout/").status_code == 405
assert client.get("/").status_code == 200
response = client.post("/logout/", {"csrfmiddlewaretoken": csrf(client, "/")})
assert response.status_code == 302 and response.url == "/login/"
assert not Session.objects.filter(session_key=authenticated_cookie).exists()
assert "_auth_user_id" not in client.session
for candidate in (client, Client(HTTP_HOST="127.0.0.1")):
    candidate.cookies[settings.SESSION_COOKIE_NAME] = authenticated_cookie
    for path in ("/", "/accounts/"):
        assert candidate.get(path).status_code == 302
''')


@pytest.mark.parametrize("case", ["wrong_password", "unknown_user", "inactive_user"])
def test_invalid_credentials_are_generic(run_django, migrated_prototype, case):
    run_django(AUTH_SETUP + "\ncase = " + json.dumps(case) + r'''
data = {}
if case == "wrong_password":
    data["password"] = secrets.token_urlsafe(24)
elif case == "unknown_user":
    data["username"] = "unknown@example.invalid"
else:
    user.is_active = False
    user.save()
response = login(client, **data)
assert response.status_code == 200
errors = response.context["form"].non_field_errors().as_data()
assert len(errors) == 1 and errors[0].code == "invalid_login"
assert str(errors[0].message) == str(response.context["form"].error_messages["invalid_login"])
assert "_auth_user_id" not in client.session
assert password not in response.content.decode()
assert data.get("password", password) not in response.content.decode()
assert b'role="alert"' in response.content
assert client.get("/").status_code == 302
''')


def test_login_fields_and_errors_are_accessible(run_django, migrated_prototype):
    run_django(AUTH_SETUP + r'''
response = client.get("/login/")
html = response.content.decode()
assert '<label for="id_username">E-posta:</label>' in html
assert '<label for="id_password">Şifre:</label>' in html
assert 'type="email"' in html and 'autocomplete="username"' in html
assert 'type="password"' in html and 'autocomplete="current-password"' in html
assert 'name="viewport"' in html and 'Yalnızca örnek veriler' in html
response = login(client, password=secrets.token_urlsafe(24))
assert 'value="sample@example.invalid"' in response.content.decode()
assert 'name="password"' in response.content.decode()
assert response.context["form"]["password"].value() is not None
# The form holds submitted input, but its PasswordInput must never render it.
assert response.context["form"]["password"].value() not in response.content.decode()
response = login(client, username="not-an-email", password="")
html = response.content.decode()
assert 'aria-invalid="true"' in html and 'id_username_error' in html
assert 'aria-describedby="id_username_error"' in html
assert 'role="alert"' in html
assert "_auth_user_id" not in client.session
''')


@pytest.mark.parametrize("destination, expected", [
    (None, "/"),
    ("/accounts/?view=cards", "/accounts/?view=cards"),
    ("http://127.0.0.1/accounts/", "http://127.0.0.1/accounts/"),
    ("https://outside.example.invalid/", "/"),
    ("//outside.example.invalid/", "/"),
    ("///outside.example.invalid/", "/"),
    (r"/\outside.example.invalid/", "/"),
    ("javascript:alert(1)", "/"),
    ("http://127.0.0.1.outside.example.invalid/", "/"),
])
def test_login_safe_redirects(run_django, migrated_prototype, destination, expected):
    run_django(AUTH_SETUP + "\ndestination = " + repr(destination) +
               "\nexpected = " + repr(expected) + r'''
overrides = {} if destination is None else {"next": destination}
response = login(client, **overrides)
assert response.status_code == 302 and response.url == expected
''')


def test_get_next_is_preserved_and_logout_destination_is_fixed(run_django, migrated_prototype):
    run_django(AUTH_SETUP + r'''
page = client.get("/login/", {"next": "/accounts/?view=cards"})
assert page.context["next"] == "/accounts/?view=cards"
token = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', page.content.decode())[1]
response = client.post("/login/", {
    "username": user.email, "password": password,
    "next": page.context["next"], "csrfmiddlewaretoken": token,
})
assert response.url == "/accounts/?view=cards"
for destination in ("/accounts/", "//outside.example.invalid/"):
    response = client.post("/logout/?next=" + destination, {
        "next": destination, "csrfmiddlewaretoken": csrf(client, "/"),
    })
    assert response.status_code == 302 and response.url == "/login/"
    assert login(client).status_code == 302
# An already signed-in user can visit login without an automatic redirect loop.
assert client.get("/login/?next=/login/").status_code == 200
''')


def test_csrf_enforcement_and_rotation(run_django, migrated_prototype):
    run_django(AUTH_SETUP + r'''
assert client.post("/login/", {"username": user.email, "password": password}).status_code == 403
token = csrf(client)
old_csrf_cookie = client.cookies["csrftoken"].value
data = {"username": user.email, "password": password, "csrfmiddlewaretoken": token}
assert client.post("/login/", dict(data, csrfmiddlewaretoken="invalid")).status_code == 403
assert client.post("/login/", data, HTTP_ORIGIN="http://outside.example.invalid").status_code == 403
assert "_auth_user_id" not in client.session
assert client.post("/login/", data, HTTP_ORIGIN="http://127.0.0.1").status_code == 302
assert client.cookies["csrftoken"].value != old_csrf_cookie
assert client.post("/logout/", {"csrfmiddlewaretoken": token}).status_code == 403
assert client.post("/logout/").status_code == 403
assert client.post("/logout/", {"csrfmiddlewaretoken": "invalid"}).status_code == 403
token = csrf(client, "/")
assert client.post("/logout/", {"csrfmiddlewaretoken": token},
                   HTTP_ORIGIN="http://outside.example.invalid").status_code == 403
assert client.get("/").status_code == 200
assert client.post("/logout/", {"csrfmiddlewaretoken": token},
                   HTTP_ORIGIN="http://127.0.0.1").status_code == 302
assert client.get("/accounts/").status_code == 302
''')


def test_session_survives_process_restart(run_django, migrated_prototype, tmp_path):
    run_django(AUTH_SETUP + r'''
assert login(client).status_code == 302
from pathlib import Path
Path("synthetic-session").write_text(client.cookies[settings.SESSION_COOKIE_NAME].value)
''')
    run_django(r'''
import django
django.setup()
from pathlib import Path
from django.conf import settings
from django.test import Client
client = Client(HTTP_HOST="127.0.0.1")
client.cookies[settings.SESSION_COOKIE_NAME] = Path("synthetic-session").read_text()
assert client.get("/accounts/").status_code == 200
''')
    assert (tmp_path / "prototype.sqlite3").stat().st_mode & 0o077 == 0


def test_only_scoped_routes_exist(run_django, migrated_prototype):
    run_django(AUTH_SETUP + r'''
for path in ("/register/", "/signup/", "/password_reset/", "/password_change/", "/admin/",
             "/accounts/1/edit/", "/accounts/1/delete/"):
    assert client.get(path).status_code == 404
''')
