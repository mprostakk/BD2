# Generated by Django 4.0 on 2022-01-16 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("discount", "0001_initial"),
        ("rent", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="discount",
            name="rent",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="rent.rent"
            ),
        ),
    ]
