# Generated by Django 5.0.1 on 2024-05-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("subject", models.CharField(max_length=50)),
                ("message", models.CharField(max_length=100)),
            ],
        ),
    ]
