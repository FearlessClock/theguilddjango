# Generated by Django 5.0.2 on 2024-03-19 15:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("tick", models.IntegerField(default=0)),
                ("tick_in_seconds", models.IntegerField(default=1)),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("start_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Goods",
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
                ("name", models.CharField(max_length=200)),
                ("perlin_noise_seed", models.IntegerField(default=123456789)),
                ("price_min", models.IntegerField(default=10)),
                ("price_max", models.IntegerField(default=40)),
            ],
        ),
        migrations.CreateModel(
            name="Storage",
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
                ("number_of_storage_spaces", models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Upgrade",
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
                ("max_level", models.IntegerField(default=5)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Character",
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
                ("name", models.CharField(max_length=200)),
                ("money", models.IntegerField(default=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.country"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GridPoint",
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
                ("x", models.IntegerField(default=0)),
                ("y", models.IntegerField(default=0)),
                ("has_building", models.BooleanField(default=False)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.country"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Building",
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
                ("type", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=40)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.country"
                    ),
                ),
                (
                    "grid_point",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.gridpoint"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                ("name", models.CharField(max_length=200)),
                ("construction_ticks", models.IntegerField(default=20)),
                (
                    "constructed_goods",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.goods"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe_Goods",
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
                ("amount_required", models.IntegerField(default=1)),
                (
                    "goods",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.goods"
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.recipe"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="recipe",
            name="required_goods",
            field=models.ManyToManyField(
                related_name="+", through="core.Recipe_Goods", to="core.goods"
            ),
        ),
        migrations.CreateModel(
            name="Stall",
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
                ("tick", models.IntegerField(default=0)),
                ("tick_in_seconds", models.IntegerField(default=1)),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("start_date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "building",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.building"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.country"
                    ),
                ),
                (
                    "storage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.storage"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("tick", models.IntegerField(default=0)),
                ("tick_in_seconds", models.IntegerField(default=1)),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("start_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("type", models.CharField(max_length=20)),
                ("location_type", models.CharField(default="workshop", max_length=20)),
                ("location_id", models.IntegerField(default=0)),
                ("current_x", models.IntegerField(default=0)),
                ("current_y", models.IntegerField(default=0)),
                ("target_x", models.IntegerField(default=0)),
                ("target_y", models.IntegerField(default=0)),
                ("travel_duration_seconds", models.IntegerField(default=1)),
                ("departure_time", models.DateTimeField(null=True)),
                ("is_traveling", models.BooleanField(default=False)),
                ("travel_speed_per_block", models.IntegerField(default=20)),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.character"
                    ),
                ),
                (
                    "storage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.storage"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Storage_Goods",
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
                ("quantity", models.IntegerField(default=0)),
                ("max_stack_size", models.IntegerField(default=20)),
                (
                    "goods_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.goods"
                    ),
                ),
                (
                    "storage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.storage"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Workshop",
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
                ("tick", models.IntegerField(default=0)),
                ("tick_in_seconds", models.IntegerField(default=1)),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("start_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("name", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=200)),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.character"
                    ),
                ),
                (
                    "storage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.storage"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=200)),
                ("is_assigned", models.BooleanField(default=False)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.country"
                    ),
                ),
                (
                    "active_recipe",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.recipe",
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.workshop",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Workshop_Recipe",
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
                ("is_available", models.BooleanField(default=False)),
                ("current_progress", models.IntegerField(default=0)),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.recipe"
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.workshop"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="workshop",
            name="recipes",
            field=models.ManyToManyField(
                through="core.Workshop_Recipe", to="core.recipe"
            ),
        ),
        migrations.CreateModel(
            name="Workshop_Upgrade",
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
                ("level", models.IntegerField(default=0)),
                (
                    "upgrade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.upgrade"
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.workshop"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="workshop",
            name="upgrade",
            field=models.ManyToManyField(
                through="core.Workshop_Upgrade", to="core.upgrade"
            ),
        ),
    ]
