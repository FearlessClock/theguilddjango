from django.db import models
from .GoodsModel import ItemInformation

class Storage(models.Model):
    quantity = models.IntegerField(default=0)
    
    class Meta:
        abstract = True

class Storage_Goods(Storage):
    goods_data = models.ForeignKey(ItemInformation, on_delete=models.CASCADE)