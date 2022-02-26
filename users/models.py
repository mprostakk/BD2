import pgtrigger
from django.contrib.auth.models import AbstractUser
from django.db import models


@pgtrigger.register(
    pgtrigger.Trigger(
        name="create_discount_on_user_create",
        operation=pgtrigger.Insert,
        when=pgtrigger.After,
        func=f"""
        INSERT INTO discount_discount (percent, start_date, end_date, user_id)
        VALUES (100, NOW(), NOW() + interval '1 year', NEW.id);
        RETURN NEW;
        """,
    )
)
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    payment_account_external_id = models.CharField(max_length=200, null=True, blank=True)

    street = models.CharField(max_length=60, null=True, blank=True)
    house_number = models.CharField(max_length=60, null=True, blank=True)
    apartment_number = models.CharField(max_length=60, null=True, blank=True)
    zip_code = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)

    @property
    def is_currently_renting(self) -> bool:
        return bool(self.rents.filter(end_time__isnull=True).first())

    @property
    def current_rent(self):
        return self.rents.filter(end_time__isnull=True).first()

    @property
    def is_payment_account_attached(self) -> bool:
        return bool(self.payment_account_external_id)

    @property
    def is_enough_money_to_rent(self) -> bool:
        mocked_enough_money = True
        return bool(self.is_payment_account_attached and mocked_enough_money)

    @property
    def is_currently_rent_break(self) -> bool:
        return bool(self.rents.filter(status="break").first())
