from django.db import models
from .WorkshopModel import Workshop

class Employee(models.Model):
    name = models.CharField(max_length=200)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    