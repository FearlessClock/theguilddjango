from TheGuild.core.Models.StorageModel import Storage, Storage_Goods
from TheGuild.core.Serializers.goods_serializer import GoodsSerializer
from rest_framework import serializers

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['id']
        
class StorageGoodsSerializer(serializers.ModelSerializer):
    goods_data = GoodsSerializer(many=False)
    class Meta:
        model = Storage_Goods
        fields = ['id', 'goods_data', 'storage', 'quantity'] 