# Generated by Django 4.0 on 2022-01-21 14:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("discount", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="percent",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
    ]
