from django.db import models
from .WorkshopModel import Workshop, Recipe
from .CountryModel import Country

class Employee(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    is_assigned = models.BooleanField(default=False)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, null=True)
    active_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    