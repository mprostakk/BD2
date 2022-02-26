from django.db import models

from users.models import CustomUser
from vehicle.models import Vehicle


class FaultReport(models.Model):
    class MalfunctionType(models.TextChoices):
        STUCK = "stuck"
        BROKEN = "broken"
        DESTROYED = "destroyed"
        OTHER = "other"

    date_reported = models.DateTimeField(auto_now_add=True)
    malfunction_type = models.CharField(max_length=20, choices=MalfunctionType.choices)
    description = models.TextField(max_length=500)

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
