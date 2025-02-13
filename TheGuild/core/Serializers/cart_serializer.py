from TheGuild.core.Models.CartModel import Cart, Cart_Storage
from rest_framework import serializers

from TheGuild.core.Serializers.goods_serializer import ItemInformationSerializer


class CartStorageSerializer(serializers.ModelSerializer):
    item_information = ItemInformationSerializer()

    class Meta:
        model = Cart_Storage
        fields = ["quantity", "item_information", "id"]


class CartSerializer(serializers.ModelSerializer):
    carried_items = CartStorageSerializer(source="cart_storage_set", many=True)

    class Meta:
        model = Cart
        fields = [
            "id",
            "type",
            "character",
            "carried_items",
            "location_type",
            "location_id",
            "current_x",
            "current_y",
            "target_x",
            "target_y",
            "travel_duration_seconds",
            "departure_time",
            "is_traveling",
        ]
