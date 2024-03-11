from django.db import models
from .GoodsModel import Goods
from .CharacterModel import Character
from .StorageModel import Storage

class Cart(models.Model):
    type = models.CharField(max_length=20)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    location_type = models.CharField(default="workshop", max_length=20)
    location_id = models.IntegerField(default=0)
    # Movement
    target_location = models.CharField(default="0,0",max_length=10)
    travel_duration_seconds = models.IntegerField(default=1)
    departure_time = models.DateTimeField(null=True)
    