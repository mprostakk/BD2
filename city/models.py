from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    zone_name = models.CharField(max_length=200)
    geometry = models.JSONField()

    def __str__(self):
        return self.zone_name
