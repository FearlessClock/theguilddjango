from django.db import models

from .ProfessionInformationModel import ProfessionInformation
from .CharacterModel import Character
from .GoodsModel import ItemInformation, Recipe
from .StorageModel import Storage
from .BuildingModel import Building
from django.contrib.auth.models import User
from .BaseTimeModel import BaseTimeModel
from datetime import datetime, UTC
from django.utils.timezone import now


class Upgrade(models.Model):
    max_level = models.IntegerField(default=5)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=200)


class Workshop(BaseTimeModel):
    name = models.CharField(max_length=200)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    upgrade = models.ManyToManyField(
        Upgrade, through="Workshop_Upgrade", through_fields=("workshop", "upgrade")
    )
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(
        Recipe, through="Workshop_Recipe", through_fields=("workshop", "recipe")
    )
    profession = models.ForeignKey(ProfessionInformation, on_delete=models.CASCADE)

    def GetWorkshopsForCharacter(character_id):
        return Workshop.objects.filter(character_id=character_id)


class Workshop_Storage(Storage):
    item_information = models.ForeignKey(ItemInformation, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "workshop",
            "item_information",
        )  # Ensure a user cannot add the same item multiple times without updating quantity


class Workshop_Upgrade(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    upgrade = models.ForeignKey(Upgrade, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)


class Workshop_Recipe(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=False)
    current_progress = models.IntegerField(default=0)
    last_update = models.DateTimeField(default=now)
