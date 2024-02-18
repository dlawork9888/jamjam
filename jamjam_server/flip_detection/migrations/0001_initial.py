# Generated by Django 5.0 on 2024-02-18 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FlipDetection",
            fields=[
                (
                    "flip_detection_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("flip_score", models.FloatField()),
                ("flip_time", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
