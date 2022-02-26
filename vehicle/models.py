from django.core.validators import MaxValueValidator
from django.db import models


class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    produced_by = models.CharField(max_length=100)
    max_speed = models.PositiveIntegerField()
    battery_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.produced_by}"


class Vehicle(models.Model):
    serial_number = models.CharField(max_length=50)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

    is_available_for_rent = models.BooleanField(default=False)
    number_of_driven_km = models.PositiveIntegerField(default=0)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    battery_level = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(100)])
    last_updated_timestamp = models.DateTimeField(null=True, auto_now=True)
    production_date = models.DateField()

    class Meta:
        unique_together = (
            "serial_number",
            "vehicle_type",
        )

    def __str__(self):
        return f"{self.serial_number} - {self.vehicle_type}"

    @property
    def is_currently_charged(self) -> bool:
        return self.battery_level >= 15.0

    @property
    def is_currently_renting(self) -> bool:
        return bool(self.rents.filter(end_time__isnull=True).first())
