from django.db import models
from .CountryModel import Country
from .StorageModel import Storage
from .BuildingModel import Building
from .BaseTimeModel import BaseTimeModel


class Stall(BaseTimeModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
