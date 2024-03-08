from django.db import models
from datetime import datetime, UTC
from .BaseTimeModel import BaseTimeModel

class Country(BaseTimeModel):
    name = models.CharField(max_length=200, unique=True)
    