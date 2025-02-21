# Generated by Django 5.0.2 on 2024-03-06 07:16
import json
from django.db import migrations
from TheGuild.core.Models.CharacterModel import Character
from TheGuild.core.Models.CountryModel import Country, GridPoint
from TheGuild.core.Models.ProfessionInformationModel import ProfessionInformation
from TheGuild.core.Models.WorkshopModel import (
    Workshop,
    Workshop_Upgrade,
    Workshop_Recipe,
)
from TheGuild.core.Models.WorkshopModel import Upgrade
from TheGuild.core.Models.EmployeeModel import Employee
from TheGuild.core.Models.GoodsModel import ItemInformation, Recipe, Recipe_Goods
from TheGuild.core.Models.CartModel import Cart
from TheGuild.core.Models.BuildingModel import Building
from TheGuild.core.Models.MarketplaceModel import Stall
from django.contrib.auth.models import User
from TheGuild.core.Models.StorageModel import Storage, Storage_Goods
from django.core.exceptions import ObjectDoesNotExist


def load_json_data():
    file = open("TheGuild/core/GameManagement/GameDataGeneration.json")
    data = json.load(file)
    file.close()
    return data


def create_users(apps, schema_editor):
    data = load_json_data()
    for userData in data["users"]:
        user = User.objects.filter(username=userData["username"])
        if not user:
            user = User.objects.create_user(
                userData["username"], userData["email"], userData["password"]
            )
            user.save()


def GenerateCountry(apps, schema_editor):
    data = load_json_data()
    for countryInfo in data["countries"]:
        if not Country.objects.filter(name=countryInfo["name"]):
            Country.objects.create(
                id=countryInfo["id"], name=countryInfo["name"]
            ).save()


def GenerateProfessionInformation(apps, schema_editor):
    data = load_json_data()
    for professionInformation in data["profession_information"]:
        if not ProfessionInformation.objects.filter(name=professionInformation["name"]):
            ProfessionInformation.objects.create(
                id=professionInformation["id"],
                name=professionInformation["name"],
                description=professionInformation["description"],
            ).save()


def GenerateGrid(apps, schema_editor):
    data = load_json_data()
    for countryData in data["countries"]:
        country = Country.objects.get(id=countryData["id"])
        try:
            GridPoint.objects.get(x=0, y=0, country=country)
            return
        except ObjectDoesNotExist:
            for x in range(countryData["grid_size"]):
                for y in range(countryData["grid_size"]):
                    GridPoint.objects.create(country=country, x=x, y=y)


def GenerateCharacters(apps, schema_editor):
    data = load_json_data()
    for charData in data["characters"]:
        if not Character.objects.filter(id=charData["id"]):
            country = Country.objects.get(id=charData["country_id"])
            user = User.objects.get(id=charData["user_id"])
            Character.objects.create(
                id=charData["id"], name=charData["name"], country=country, user=user
            )


def GenerateUpgrades(apps, schema_editor):
    data = load_json_data()
    for upgrade in data["upgrades"]:
        if not Upgrade.objects.filter(id=upgrade["id"]):
            Upgrade.objects.create(
                id=upgrade["id"],
                name=upgrade["name"],
                max_level=upgrade["max_level"],
                price=upgrade["price"],
            )


def GenerateGoods(apps, schema_editor):
    data = load_json_data()
    for goods_data in data["goods_data"]:
        if not ItemInformation.objects.filter(id=goods_data["id"]):
            ItemInformation.objects.create(
                id=goods_data["id"],
                name=goods_data["name"],
                perlin_noise_seed=goods_data["perlin_noise_seed"],
                price_min=goods_data["price_min"],
                price_max=goods_data["price_max"],
            )


def GenerateRecipes(apps, schema_editor):
    data = load_json_data()
    for recipe in data["recipes"]:
        if not Recipe.objects.filter(id=recipe["id"]):
            rep = Recipe.objects.create(
                id=recipe["id"],
                name=recipe["name"],
                construction_ticks=recipe["construction_ticks"],
                constructed_goods=ItemInformation.objects.get(
                    id=recipe["constructed_goods"]
                ),
            )
            for req_goods in recipe["required_goods"]:
                Recipe_Goods.objects.create(
                    recipe=rep,
                    goods=ItemInformation.objects.get(id=req_goods["goods_data_id"]),
                    amount_required=req_goods["amount_required"],
                )


def GenerateEmployees(apps, schema_editor):
    data = load_json_data()
    for employee in data["employees"]:
        if not Employee.objects.filter(name=employee["name"]):
            country = Country.objects.get(id=employee["country"])
            Employee.objects.create(
                id=employee["id"], name=employee["name"], country=country
            )


def GenerateWorkshop(apps, schema_editor):
    data = load_json_data()
    for json in data["workshops"]:
        if not Workshop.objects.filter(id=json["id"]):
            char = Character.objects.get(id=json["character_id"])
            grid_point = GridPoint.objects.get(
                x=json["x"], y=json["y"], country=char.country
            )
            building = Building.objects.create(
                country=char.country,
                grid_point=grid_point,
                type=json["type"],
                name=json["name"],
            )
            grid_point.has_building = True
            grid_point.save()
            storage = Storage.objects.create(
                number_of_storage_spaces=json["number_of_storage_spaces"]
            )
            workshop = Workshop.objects.create(
                id=json["id"], building=building, character=char, storage=storage
            )
            for ups in json["upgrades"]:
                upgrade = Upgrade.objects.get(id=ups["id"])
                Workshop_Upgrade.objects.create(
                    workshop=workshop, upgrade=upgrade, level=ups["level"]
                )
            for recipe in json["recipes"]:
                Workshop_Recipe.objects.create(
                    workshop=workshop,
                    recipe=Recipe.objects.get(id=recipe["id"]),
                    is_available=recipe["is_available"],
                )
            for goods in json["goods"]:
                Storage_Goods.objects.create(
                    storage=storage,
                    goods_data=ItemInformation.objects.get(id=goods["id"]),
                    quantity=goods["quantity"],
                )


def GenerateCarts(apps, schema_editor):
    data = load_json_data()
    for cart in data["carts"]:
        if not Cart.objects.filter(id=cart["id"]):
            storage = Storage.objects.create(
                number_of_storage_spaces=cart["number_of_storage_spaces"]
            )
            Cart.objects.create(
                id=cart["id"],
                type=cart["type"],
                character=Character.objects.get(id=cart["character"]),
                storage=storage,
                location_type=cart["location_type"],
                location_id=Workshop.GetWorkshopsForCharacter(cart["character"])
                .first()
                .building.id,
                current_x=cart["x"],
                current_y=cart["y"],
                is_traveling=cart["is_traveling"],
            )


def GenerateStalls(apps, schema_editor):
    data = load_json_data()
    for stall in data["stalls"]:
        if not Stall.objects.filter(id=stall["id"]):
            country = Country.objects.get(id=stall["id"])
            storage = Storage.objects.create(
                number_of_storage_spaces=stall["number_of_storage_spaces"]
            )
            grid_point = GridPoint.objects.get(
                x=stall["x"], y=stall["y"], country=country
            )
            building = Building.objects.create(
                country=country,
                grid_point=grid_point,
                type=stall["type"],
                name=stall["name"],
            )
            Stall.objects.create(
                id=stall["id"], country=country, storage=storage, building=building
            )
            grid_point.has_building = True
            grid_point.save()
            for goods in stall["goods"]:
                Storage_Goods.objects.create(
                    storage=storage,
                    goods_data=ItemInformation.objects.get(id=goods["id"]),
                    quantity=goods["quantity"],
                )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_professioninformation"),
    ]

    operations = [
        migrations.RunPython(create_users),
        migrations.RunPython(GenerateCountry),
        migrations.RunPython(GenerateProfessionInformation),
        migrations.RunPython(GenerateGrid),
        migrations.RunPython(GenerateCharacters),
        migrations.RunPython(GenerateUpgrades),
        migrations.RunPython(GenerateGoods),
        migrations.RunPython(GenerateRecipes),
        migrations.RunPython(GenerateWorkshop),
        migrations.RunPython(GenerateEmployees),
        migrations.RunPython(GenerateCarts),
        migrations.RunPython(GenerateStalls),
    ]
