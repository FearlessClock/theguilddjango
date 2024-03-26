from TheGuild.core.Models.WorkshopModel import Workshop, Upgrade, Workshop_Recipe
from TheGuild.core.Serializers.goods_serializer import RecipeSerializer, RecipeWithGoodsSerializer
from TheGuild.core.Serializers.core_serializer import BuildingSerializer
from rest_framework import serializers

class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgrade
        fields = ['id', 'max_level', 'name']
        
class WorkshopSerializer(serializers.ModelSerializer):
    building=BuildingSerializer(many=False)
    class Meta:
        model = Workshop
        fields = ['id', 'character', 'building', 'storage', 'upgrade', 'tick', 'last_update']
        
class WorkshopRecipeWithFullRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeWithGoodsSerializer(many=False)
    class Meta:
        model = Workshop_Recipe
        fields = ['id', 'workshop', 'recipe', 'is_available', 'current_progress', 'last_update']