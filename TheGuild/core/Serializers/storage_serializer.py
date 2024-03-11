from TheGuild.core.Models.StorageModel import Storage, Storage_Goods
from rest_framework import serializers

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['id']
        
class StorageGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage_Goods
        fields = ['id', 'goods_data', 'storage', 'quantity']