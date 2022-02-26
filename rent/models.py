import decimal

from django.db import models

from city.models import City
from scooters.settings import MINUTE_RENT_BREAK_COST, MINUTE_RENT_COST, START_RENT_COST
from users.models import CustomUser
from vehicle.models import Vehicle


class Rent(models.Model):
    class Status(models.TextChoices):
        START = "start"
        END = "end"
        DURING = "during"
        BREAK = "break"

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="rents")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="rents")  # !
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.START)
    payment_external_id = models.CharField(max_length=200, null=True)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    ended_in_allowed_zone = models.BooleanField(null=True)

    @property
    def total_cost_display(self):
        if self.total_cost:
            return f"{self.total_cost} PLN"
        return ""

    @property
    def is_currently_in_break(self) -> bool:
        return bool(self.current_rent_break)

    @property
    def current_rent_break(self):
        return self.rent_breaks.filter(end_time__isnull=True).first()

    def calculate_total_cost(self) -> decimal.Decimal:
        delta_rent = self.end_time - self.start_time
        rent_minutes = delta_rent.seconds / 60

        break_minutes = 0
        for rent_break in self.rent_breaks.all():
            delta_rent_break = rent_break.end_time - rent_break.start_time
            break_minutes += delta_rent_break.seconds / 60

        rent_minutes -= break_minutes
        return decimal.Decimal(
            START_RENT_COST
            + rent_minutes * MINUTE_RENT_COST
            + break_minutes * MINUTE_RENT_BREAK_COST
        )


class RentBreak(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, related_name="rent_breaks")

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
