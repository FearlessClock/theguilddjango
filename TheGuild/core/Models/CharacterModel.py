from django.db import models
from .CountryModel import Country
from django.contrib.auth.models import User

class Character(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)