# Generated by Django 5.0.2 on 2024-03-16 16:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_gridpoint_building_stall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='target_location',
        ),
        migrations.AddField(
            model_name='cart',
            name='current_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='current_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='is_traveling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='target_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='target_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='tick',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='tick_in_seconds',
            field=models.IntegerField(default=1),
        ),
    ]