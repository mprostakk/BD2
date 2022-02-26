from django.core.validators import MaxValueValidator
from django.db import models

from rent.models import Rent
from users.models import CustomUser


class Discount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, null=True)

    percent = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
