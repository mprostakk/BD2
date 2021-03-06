# Generated by Django 4.0 on 2022-01-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("percent", models.PositiveSmallIntegerField()),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
            ],
        ),
    ]
