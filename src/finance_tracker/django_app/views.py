"""Synthetic presentation only; no ORM queries, financial logic or network calls."""

from django.shortcuts import render
from django.views.decorators.http import require_safe


@require_safe
def dashboard(request):
    return render(request, "prototype/dashboard.html", {"active_page": "dashboard"})


@require_safe
def accounts(request):
    return render(request, "prototype/accounts.html", {"active_page": "accounts"})
