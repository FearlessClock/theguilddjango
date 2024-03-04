from django.db import models
from .CountryModel import Country
from django.contrib.auth.models import User

class Upgrade(models.Model):
    max_level = models.IntegerField(default=5)
    name = models.CharField(max_length=200)
    
class Workshop(models.Model):
    character = models.ForeignKey(Country, on_delete=models.CASCADE)
    upgrade = models.ManyToManyField(Upgrade, through="Workshop_Upgrade",
                                                through_fields=("workshop", "upgrade"))
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    
class workshop_upgrade(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    upgrade = models.ForeignKey(Upgrade, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)