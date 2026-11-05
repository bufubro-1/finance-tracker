"""Local prototype routes; no registration, admin or non-opening financial writes."""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .identity.forms import PrototypeAuthenticationForm

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="prototype/login.html",
        authentication_form=PrototypeAuthenticationForm,
    ), name="login"),
    path("logout/", LogoutView.as_view(redirect_field_name=None), name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("accounts/", views.accounts, name="accounts"),
    path("accounts/create/", views.create_account, name="create_account"),
]
