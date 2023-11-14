# Generated by Django 4.2.6 on 2023-11-14 14:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="events", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
