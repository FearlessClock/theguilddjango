from django.db import models
from .CharacterModel import Character
from .GoodsModel import Goods, Recipe
from django.contrib.auth.models import User
from .BaseTimeModel import BaseTimeModel
from datetime import datetime, UTC

class Upgrade(models.Model):
    max_level = models.IntegerField(default=5)
    name = models.CharField(max_length=200)
    
class Workshop(BaseTimeModel):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    upgrade = models.ManyToManyField(Upgrade, through="Workshop_Upgrade",
                                                through_fields=("workshop", "upgrade"))
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    stored_goods = models.ManyToManyField(Goods, through="Workshop_Goods", through_fields=("workshop", "goods_data"))
    recipes = models.ManyToManyField(Recipe, through="Workshop_Recipe", through_fields=("workshop", "recipe"))

    def UpdateWorkshops(self):
        secondsSinceLastUpdate = (datetime.now(UTC) - self.last_update).total_seconds()
        if secondsSinceLastUpdate > self.tick_in_seconds:
            self.last_update = datetime.now(UTC)
            self.tick = int((datetime.now(UTC) - self.start_date).total_seconds() / self.tick_in_seconds)
            self.save()
        
    
class Workshop_Upgrade(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    upgrade = models.ForeignKey(Upgrade, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    
class Workshop_Goods(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    goods_data = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
class Workshop_Recipe(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=False)