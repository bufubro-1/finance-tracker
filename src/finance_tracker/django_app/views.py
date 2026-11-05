"""Authenticated synthetic presentation; no financial queries or external calls."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_safe


@never_cache
@require_safe
@login_required
def dashboard(request):
    return render(request, "prototype/dashboard.html", {"active_page": "dashboard"})


@never_cache
@require_safe
@login_required
def accounts(request):
    return render(request, "prototype/accounts.html", {"active_page": "accounts"})
