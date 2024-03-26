from TheGuild.core.Models.EmployeeModel import Employee
from rest_framework import serializers
from TheGuild.core.Serializers.goods_serializer import RecipeSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    active_recipe = RecipeSerializer(many=False)
    class Meta:
        model = Employee
        fields = ['id', 'name', 'is_assigned', 'workshop', 'active_recipe', 'country_id']