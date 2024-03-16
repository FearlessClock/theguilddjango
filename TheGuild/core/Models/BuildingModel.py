from django.db import models
from .CountryModel import Country, GridPoint

class Building(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    grid_point = models.ForeignKey(GridPoint, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=40)