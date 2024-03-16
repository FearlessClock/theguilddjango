from django.db import models
from .GoodsModel import Goods
from .CharacterModel import Character
from .StorageModel import Storage
from .CountryModel import GridPoint
from .BuildingModel import Building
from .BaseTimeModel import BaseTimeModel
from datetime import datetime, UTC

class Cart(BaseTimeModel):
    type = models.CharField(max_length=20)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    location_type = models.CharField(default="workshop", max_length=20)
    location_id = models.IntegerField(default=0)
    # Movement
    current_x = models.IntegerField(default=0)
    current_y = models.IntegerField(default=0)
    target_x = models.IntegerField(default=0)
    target_y = models.IntegerField(default=0)
    travel_duration_seconds = models.IntegerField(default=1)
    departure_time = models.DateTimeField(null=True)
    is_traveling = models.BooleanField(default=False)
    travel_speed_per_block = models.IntegerField(default=20)
    
    def UpdateCart(self):
        secondsSinceLastUpdate = (datetime.now(UTC) - self.last_update).total_seconds()
        if secondsSinceLastUpdate <= self.tick_in_seconds:
            return
        self.last_update = datetime.now(UTC)
        if not self.is_traveling:
            return
        progress = (datetime.now(UTC) - self.departure_time).total_seconds()
        if progress >= self.travel_duration_seconds:
                self.is_traveling = False
                self.current_x = self.target_x
                self.current_y = self.target_y
                
                gridPoint = GridPoint.objects.get(x=self.current_x, y=self.current_y, country=self.character.country)
                if not gridPoint.has_building:
                    self.location_id = -1
                    self.location_type = ""
                else:
                    building = Building.objects.filter(grid_point_id=gridPoint.id, country=self.character.country)
                    self.location_id = building.id
                    self.location_type = building.type
                self.save()
        