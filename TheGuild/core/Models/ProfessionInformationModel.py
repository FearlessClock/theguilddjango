from django.db import models
from datetime import datetime, UTC
from .BaseTimeModel import BaseTimeModel

class ProfessionInformation(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000)