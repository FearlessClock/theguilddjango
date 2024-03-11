from django.db import models
from .GoodsModel import Goods

class Storage(models.Model):
    number_of_storage_spaces = models.IntegerField(default=1)

class Storage_Goods(models.Model):
    goods_data = models.ForeignKey(Goods, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    max_stack_size = models.IntegerField(default=20)