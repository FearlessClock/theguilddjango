from TheGuild.core.Models.GoodsModel import ItemInformation, Recipe_Goods, Recipe
from rest_framework import serializers


class ItemInformationSerializer(serializers.ModelSerializer):
    current_price = serializers.SerializerMethodField()

    class Meta:
        model = ItemInformation
        fields = [
            "id",
            "name",
            "perlin_noise_seed",
            "price_min",
            "price_max",
            "current_price",
        ]

    def get_current_price(self, obj: ItemInformation):
        return obj.GetCurrentPrice()


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "required_goods",
            "constructed_goods",
            "construction_ticks",
        ]


class RecipeGoodsSerializer(serializers.ModelSerializer):
    goods = ItemInformationSerializer(many=False)

    class Meta:
        model = Recipe_Goods
        fields = ["id", "recipe", "goods", "amount_required"]


class RecipeWithGoodsSerializer(serializers.ModelSerializer):
    required_goods = serializers.SerializerMethodField()
    constructed_goods = ItemInformationSerializer(many=False)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "required_goods",
            "constructed_goods",
            "construction_ticks",
        ]

    def get_required_goods(self, obj):
        goods = Recipe_Goods.objects.filter(recipe_id=obj.id)
        res = []
        for good in goods:
            print(good)
            res.append(RecipeGoodsSerializer(good).data)
        return res
