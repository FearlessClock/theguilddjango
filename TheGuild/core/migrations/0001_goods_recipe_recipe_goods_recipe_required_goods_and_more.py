# Generated by Django 5.0.2 on 2024-03-06 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('perlin_noise_seed', models.IntegerField(default=123456789)),
                ('price_min', models.IntegerField(default=10)),
                ('price_max', models.IntegerField(default=40)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('construction_ticks', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_required', models.IntegerField(default=1)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.goods')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='required_goods',
            field=models.ManyToManyField(through='core.Recipe_Goods', to='core.goods'),
        ),
        migrations.CreateModel(
            name='Workshop_Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('goods_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.goods')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.workshop')),
            ],
        ),
        migrations.AddField(
            model_name='workshop',
            name='stored_goods',
            field=models.ManyToManyField(through='core.Workshop_Goods', to='core.goods'),
        ),
        migrations.CreateModel(
            name='Workshop_Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.recipe')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.workshop')),
            ],
        ),
        migrations.AddField(
            model_name='workshop',
            name='recipes',
            field=models.ManyToManyField(through='core.Workshop_Recipe', to='core.recipe'),
        ),
    ]
