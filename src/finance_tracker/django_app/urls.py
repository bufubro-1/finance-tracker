"""Read-only shell routes. No login, admin, account writes or external endpoints."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("accounts/", views.accounts, name="accounts"),
]
