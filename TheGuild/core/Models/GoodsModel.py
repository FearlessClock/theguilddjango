from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=200)
    perlin_noise_seed = models.IntegerField(default=123456789)
    price_min = models.IntegerField(default=10)
    price_max = models.IntegerField(default=40)
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    required_goods = models.ManyToManyField(Goods, related_name="+", through="Recipe_Goods", through_fields=("recipe", "goods"))
    constructed_goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    construction_ticks = models.IntegerField(default=20)
    
class Recipe_Goods(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    amount_required = models.IntegerField(default=1)
    