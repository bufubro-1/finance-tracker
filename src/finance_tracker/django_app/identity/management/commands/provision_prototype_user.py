"""Explicit, interactive provisioning for the disposable local prototype only."""

import getpass
from pathlib import Path
import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import DatabaseError, transaction
from django.views.decorators.debug import sensitive_variables


class Command(BaseCommand):
    help = "Provision sample@example.invalid in the local synthetic prototype only."

    @sensitive_variables("password", "confirmation")
    def handle(self, *args, **options):
        if (settings.SETTINGS_MODULE != "finance_tracker.django_app.settings"
                or settings.DATABASES["default"]["ENGINE"] != "django.db.backends.sqlite3"):
            raise CommandError("Synthetic provisioning requires the SQLite prototype settings.")

        User = get_user_model()
        email = "sample@example.invalid"
        if not Path(settings.DATABASES["default"]["NAME"]).is_file():
            raise CommandError("Prototype database unavailable. Run the documented migrations first.")
        try:
            if User.objects.filter(email__iexact=email).exists():
                raise CommandError("Synthetic identity already exists; no changes made.")
        except DatabaseError:
            raise CommandError("Prototype database unavailable. Run the documented migrations first.") from None

        try:
            with warnings.catch_warnings():
                # Never fall back to visible input when a terminal is unavailable.
                warnings.simplefilter("error", getpass.GetPassWarning)
                password = getpass.getpass("Synthetic identity password: ")
                confirmation = getpass.getpass("Confirm password: ")
        except (EOFError, KeyboardInterrupt, getpass.GetPassWarning):
            raise CommandError("Password entry canceled or secure terminal unavailable; no user created.") from None
        if not password.strip() or password != confirmation:
            raise CommandError("Passwords must be nonblank and match; no user created.")

        try:
            with transaction.atomic():
                User.objects.create_user(
                    email, password, is_active=True, is_staff=False, is_superuser=False,
                )
        except DatabaseError:
            raise CommandError("Could not create the synthetic identity; no existing user changed.") from None
        self.stdout.write(self.style.SUCCESS(f"Created {email}. Synthetic development only."))
