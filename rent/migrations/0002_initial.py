# Generated by Django 4.0 on 2022-01-16 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rent", "0001_initial"),
        ("vehicle", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rent",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rents",
                to="users.customuser",
            ),
        ),
        migrations.AddField(
            model_name="rent",
            name="vehicle",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vehicle.vehicle"
            ),
        ),
    ]