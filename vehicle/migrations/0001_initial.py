# Generated by Django 4.0 on 2022-01-16 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VehicleType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("produced_by", models.CharField(max_length=100)),
                ("max_speed", models.PositiveIntegerField()),
                ("battery_capacity", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("serial_number", models.CharField(max_length=50)),
                ("is_available_for_rent", models.BooleanField(default=False)),
                ("number_of_driven_km", models.PositiveIntegerField(default=0)),
                ("longitude", models.FloatField(null=True)),
                ("latitude", models.FloatField(null=True)),
                ("battery_level", models.FloatField(null=True)),
                ("last_updated_timestamp", models.DateTimeField(null=True)),
                ("production_date", models.DateField()),
                (
                    "vehicle_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="vehicle.vehicletype"
                    ),
                ),
            ],
        ),
    ]
