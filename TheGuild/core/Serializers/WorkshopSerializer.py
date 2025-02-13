from TheGuild.core.Models.WorkshopModel import (
    Workshop,
    Upgrade,
    Workshop_Recipe,
    Workshop_Storage,
)
from TheGuild.core.Serializers.goods_serializer import (
    ItemInformationSerializer,
    RecipeSerializer,
    RecipeWithGoodsSerializer,
)
from TheGuild.core.Serializers.core_serializer import BuildingSerializer
from rest_framework import serializers


class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgrade
        fields = ["id", "max_level", "name"]


class WorkshopStorageSerializer(serializers.ModelSerializer):
    item_information = ItemInformationSerializer()

    class Meta:
        model = Workshop_Storage
        fields = ["quantity", "item_information", "id"]


class WorkshopSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(many=False)
    carried_items = WorkshopStorageSerializer(source="workshop_storage_set", many=True)

    class Meta:
        model = Workshop
        fields = [
            "id",
            "character",
            "building",
            "carried_items",
            "upgrade",
            "tick",
            "last_update",
        ]


class WorkshopRecipeWithFullRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeWithGoodsSerializer(many=False)

    class Meta:
        model = Workshop_Recipe
        fields = [
            "id",
            "workshop",
            "recipe",
            "is_available",
            "current_progress",
            "last_update",
        ]
