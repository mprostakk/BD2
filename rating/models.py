from django.core.validators import MaxValueValidator
from django.db import models

from rent.models import Rent
from users.models import CustomUser


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    score = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    description = models.TextField(max_length=500, null=True, blank=True)
