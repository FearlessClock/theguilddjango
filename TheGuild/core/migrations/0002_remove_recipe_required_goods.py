# Generated by Django 5.0.2 on 2024-03-22 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_goods_last_update_goods_start_date_goods_tick_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='required_goods',
        ),
    ]