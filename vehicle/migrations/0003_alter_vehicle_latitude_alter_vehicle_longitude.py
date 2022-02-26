# Generated by Django 4.0 on 2022-01-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0002_alter_vehicle_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]