# Generated by Django 5.0.2 on 2024-03-04 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0003_upgrade_workshop_workshop_upgrade_workshop_upgrade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='country_id',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='user_id',
            new_name='user',
        ),
    ]
