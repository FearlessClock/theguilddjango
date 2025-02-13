# Generated by Django 5.0.2 on 2024-03-22 19:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_remove_workshop_name_remove_workshop_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="goods",
            name="last_update",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="goods",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="goods",
            name="tick",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="goods",
            name="tick_in_seconds",
            field=models.IntegerField(default=1),
        ),
    ]
