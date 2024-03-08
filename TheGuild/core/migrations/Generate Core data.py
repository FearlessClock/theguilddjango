# Generated by Django 5.0.2 on 2024-03-06 07:16

from django.db import migrations
from TheGuild.core.Models.CharacterModel import Character
from TheGuild.core.Models.CountryModel import Country
from TheGuild.core.Models.WorkshopModel import Workshop, Workshop_Upgrade, Workshop_Recipe, Workshop_Goods
from TheGuild.core.Models.WorkshopModel import Upgrade
from TheGuild.core.Models.EmployeeModel import Employee
from TheGuild.core.Models.GoodsModel import Goods, Recipe, Recipe_Goods
from django.contrib.auth.models import User

def create_users(apps, schema_editor):
    user = User.objects.filter(username="AmusedSandpaper")
    if not user:
        user = User.objects.create_user("AmusedSandpaper", "Amusing@email.com","abcde12345")
        user.save()
    user = User.objects.filter(username="JohnsUser")
    if not user:
        user = User.objects.create_user("JohnsUser", "Amusing@email.com","abcde12345")
        user.save()
    user = User.objects.filter(username="UncleBensUser")
    if not user:
        user = User.objects.create_user("UncleBensUser", "Amusing@email.com","abcde12345")
        user.save()
        
def GenerateCharacters(apps, schema_editor):
    country = Country.objects.get(id=1)
    if(not Character.objects.filter(name="Pieter")):
        user = User.objects.get(id=1)
        Character.objects.create(name="Pieter", country=country, user=user)
    
    if(not Character.objects.filter(name="Jack")):
        user = User.objects.get(id=2)
        Character.objects.create(name="Jack", country=country, user=user)
        
    if(not Character.objects.filter(name="Mark")):
        user = User.objects.get(id=1)
        country = Country.objects.get(id=2)
        Character.objects.create(name="Mark", country=country, user=user)
        
    if(not Character.objects.filter(name="Bob")):
        user = User.objects.get(id=3)
        country = Country.objects.get(id=3)
        Character.objects.create(name="Bob", country=country, user=user)
    
def GenerateCountry(apps, schema_editor):
    if(not Country.objects.filter(name="France")):
        Country.objects.create(name="France")
    if(not Country.objects.filter(name="Britain")):
        Country.objects.create(name="Britain")
    if(not Country.objects.filter(name="Belgium")):
        Country.objects.create(name="Belgium")
    
def GenerateUpgrades(apps, schema_editor):
    if(not Upgrade.objects.filter(name="Bars")):
        Upgrade.objects.create(name="Bars", max_level=5)
    if(not Upgrade.objects.filter(name="Roof")):
        Upgrade.objects.create(name="Roof", max_level=4)
    if(not Upgrade.objects.filter(name="Power hammer")):
        Upgrade.objects.create(name="Power hammer", max_level=7)
    
def GenerateGoods(apps, schema_editor):
    if(not Goods.objects.filter(name="Wood")):
        Goods.objects.create(name="Wood", perlin_noise_seed=123, price_min=20,price_max=100)
    if(not Goods.objects.filter(name="Stone")):
        Goods.objects.create(name="Stone", perlin_noise_seed=223, price_min=50,price_max=70)
    if(not Goods.objects.filter(name="Iron")):
        Goods.objects.create(name="Iron", perlin_noise_seed=524, price_min=10,price_max=20)
    if(not Goods.objects.filter(name="Statue")):
        Goods.objects.create(name="Statue", perlin_noise_seed=234, price_min=40,price_max=200)
    if(not Goods.objects.filter(name="Sword")):
        Goods.objects.create(name="Sword", perlin_noise_seed=222, price_min=60,price_max=110)
    
def GenerateRecipes(apps, schema_editor):
    if(not Recipe.objects.filter(name="Statue")):
        Recipe.objects.create(name="Statue", construction_ticks=40, 
                            constructed_goods=Goods.objects.get(id=4))
        recipe_goods_wood = Recipe_Goods.objects.create(
            recipe = Recipe.objects.get(id=1),
            goods = Goods.objects.get(id=1),
            amount_required = 2
        )
    if(not Recipe.objects.filter(name="Sword")):
        Recipe.objects.create(name="Sword", construction_ticks=32, 
                            constructed_goods=Goods.objects.get(id=5))
        recipe_goods_stone = Recipe_Goods.objects.create(
            recipe = Recipe.objects.get(id=2),
            goods = Goods.objects.get(id=2),
            amount_required = 1
        )
        recipe_goods_iron = Recipe_Goods.objects.create(
            recipe = Recipe.objects.get(id=2),
            goods = Goods.objects.get(id=3),
            amount_required = 2
        )
    
def GenerateEmployees(apps, schema_editor):
    country = Country.objects.get(id=1)
    if(not Employee.objects.filter(name="Jonny")):
        Employee.objects.create(name="Jonny", country=country)
    if(not Employee.objects.filter(name="Markus")):
        Employee.objects.create(name="Markus", country=country)
    if(not Employee.objects.filter(name="Sam")):
        Employee.objects.create(name="Sam", country=country)
    if(not Employee.objects.filter(name="Pirre")):
        Employee.objects.create(name="Pierre", country=country)
    if(not Employee.objects.filter(name="Fred")):
        Employee.objects.create(name="Fred", country=country)
    country = Country.objects.get(id=2)
    if(not Employee.objects.filter(name="James")):
        Employee.objects.create(name="James", country=country)
    if(not Employee.objects.filter(name="Mike")):
        Employee.objects.create(name="Mike", country=country)

def GenerateWorkshop(apps, schema_editor):
    Char = Character
    if(not Workshop.objects.filter(name="Sword and Shield")):
        char = Char.objects.get(id=1)
        workshop = Workshop.objects.create(type="Blacksmith", name="Sword and Shield", character=char)
        upgrade = Upgrade.objects.get(id=1)
        Workshop_Upgrade(
            workshop = workshop,
            upgrade = upgrade,
            level = 1
        ).save()
        Workshop_Recipe(
            workshop = workshop,
            recipe = Recipe.objects.get(id=1),
            is_available = True
        ).save()
        Workshop_Recipe(
            workshop = workshop,
            recipe = Recipe.objects.get(id=2),
            is_available = False
        ).save()
        Workshop_Goods.objects.create(
            workshop = workshop,
            goods_data = Goods.objects.get(id=1),
            quantity = 10
        )
        Workshop_Goods.objects.create(
            workshop = workshop,
            goods_data = Goods.objects.get(id=2),
            quantity = 5
        )
    if(not Workshop.objects.filter(name="Taning shop")):
        char = Char.objects.get(id=2)
        workshop = Workshop.objects.create(type="Tanner", name="Taning shop", character=char)
        
    if(not Workshop.objects.filter(name="Joining wood")):
        char = Char.objects.get(id=3)
        workshop = Workshop.objects.create(type="Joinery", name="Joining wood", character=char) 
        
    if(not Workshop.objects.filter(name="Booking a chat")):
        char = Char.objects.get(id=4)
        workshop = Workshop.objects.create(type="Coffee shop", name="Booking a chat", character=char)
    
    
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_recipe_constructed_goods_alter_recipe_required_goods'),
    ]

    operations = [
        migrations.RunPython(create_users),
        migrations.RunPython(GenerateCountry),
        migrations.RunPython(GenerateCharacters),
        migrations.RunPython(GenerateUpgrades),
        migrations.RunPython(GenerateGoods),
        migrations.RunPython(GenerateRecipes),
        migrations.RunPython(GenerateWorkshop),
        migrations.RunPython(GenerateEmployees),
    ]
