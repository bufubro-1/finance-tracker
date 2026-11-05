"""Authenticated synthetic account pages; all owner context comes from the session."""

from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods, require_safe

from .forms import AccountCreationForm
from .services import CreationError, create_savings_account, recorded_accounts, require_owner


@never_cache
def csrf_failure(request, reason=""):
    # Do not reflect the middleware reason or submitted values into the response.
    return render(request, "prototype/csrf_error.html", status=403)


@never_cache
@require_safe
@login_required
def dashboard(request):
    return render(request, "prototype/dashboard.html", {
        "active_page": "dashboard", **recorded_accounts(request.user),
    })


@never_cache
@require_safe
@login_required
def accounts(request):
    context = {"active_page": "accounts", **recorded_accounts(request.user)}
    # Only acknowledge a saved object owned by this session; never echo query-string names.
    context["saved"] = any(str(card["id"]) == request.GET.get("saved") for card in context["accounts"])
    return render(request, "prototype/accounts.html", context)


@never_cache
@login_required
@require_http_methods(["GET", "POST"])
def create_account(request):
    require_owner(request.user)
    form = AccountCreationForm(
        request.POST if request.method == "POST" else None,
        initial={"submission_key": uuid4()},
    )
    if request.method == "POST" and form.is_valid():
        try:
            result = create_savings_account(request.user, **form.cleaned_data)
        except CreationError as error:
            form.add_error(error.field, str(error))
        else:
            return redirect(f"{reverse('accounts')}?saved={result.account.pk}")
    return render(request, "prototype/account_form.html", {"active_page": "accounts", "form": form})
