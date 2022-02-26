# Generated by Django 4.0 on 2022-01-19 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0006_alter_rentbreak_end_time_alter_rentbreak_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentbreak",
            name="rent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rent_breaks",
                to="rent.rent",
            ),
        ),
    ]
