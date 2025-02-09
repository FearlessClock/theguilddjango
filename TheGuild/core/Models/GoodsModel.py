from django.db import models
from noise import pnoise1
from .BaseTimeModel import BaseTimeModel
from datetime import datetime, UTC

class ItemInformation(BaseTimeModel):
    name = models.CharField(max_length=200)
    perlin_noise_seed = models.IntegerField(default=123456789)
    price_min = models.IntegerField(default=10)
    price_max = models.IntegerField(default=40)
    
    def Remap(self, value, oldMin, oldMax, newMin, newMax):
        return (((value - oldMin) * (newMax - newMin)) / (oldMax - oldMin)) + newMin
    
    def GetCurrentPrice(self):
        self.TickGoods()
        octaves = 1
        x = self.tick * 0.002
        return int(self.Remap(int(pnoise1(x / 16.0*octaves, octaves) * 127.0 + 128.0), 0.0, 250, self.price_min, self.price_max))
    
    def TickGoods(self):
        secondsSinceLastUpdate = (datetime.now(UTC) - self.last_update).total_seconds()
        if secondsSinceLastUpdate > self.tick_in_seconds:
            self.last_update = datetime.now(UTC)
            self.tick = int((datetime.now(UTC) - self.start_date).total_seconds() / self.tick_in_seconds)
            self.save()
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    constructed_item_information = models.ForeignKey(ItemInformation, on_delete=models.CASCADE)
    construction_ticks = models.IntegerField(default=20)
    
class Recipe_Goods(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    goods = models.ForeignKey(ItemInformation, on_delete=models.CASCADE)
    amount_required = models.IntegerField(default=1)
    