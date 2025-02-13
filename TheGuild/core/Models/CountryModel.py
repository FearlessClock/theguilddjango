from django.db import models
from datetime import datetime, UTC
from .BaseTimeModel import BaseTimeModel


class Country(BaseTimeModel):
    name = models.CharField(max_length=200, unique=True)


class GridPoint(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    has_building = models.BooleanField(default=False)
