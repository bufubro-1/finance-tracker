"""Reusable opening-only ORM subset. All records are disposable and synthetic."""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .account_rules import MAX_MINOR


class UserSettings(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    reporting_currency = models.CharField(max_length=3)
    minor_unit_scale = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [models.CheckConstraint(
            condition=models.Q(reporting_currency="USD", minor_unit_scale=2),
            name="prototype_usd_scale_two",
        )]


class Account(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    normalized_name = models.CharField(max_length=300)
    kind = models.CharField(max_length=10, default="savings", editable=False)
    # Minimal prototype creation guard, committed with the opening observation.
    # These are not a general update-batch or release concurrency implementation.
    creation_key = models.UUIDField(editable=False)
    creation_fingerprint = models.CharField(max_length=64, editable=False)
    created_at = models.DateTimeField(editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["owner", "normalized_name"], name="prototype_owner_account_name"),
            models.UniqueConstraint(fields=["owner", "creation_key"], name="prototype_owner_creation_key"),
            models.CheckConstraint(condition=models.Q(kind="savings"), name="prototype_savings_only"),
        ]
        ordering = ["name", "pk"]


class BalanceObservation(models.Model):
    # Owner is inherited from this mandatory account; clients never supply it.
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="observations")
    cash_minor = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(MAX_MINOR)])
    effective_date = models.DateField()
    recorded_at = models.DateTimeField(editable=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cash_minor__gte=0, cash_minor__lte=MAX_MINOR),
                name="prototype_cash_minor_range",
            ),
            # Opening-only slice; a later reviewed migration can allow dated updates.
            models.UniqueConstraint(fields=["account"], name="prototype_one_opening_per_account"),
        ]
