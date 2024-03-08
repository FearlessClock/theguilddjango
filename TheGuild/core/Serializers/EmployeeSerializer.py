from TheGuild.core.Models.EmployeeModel import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'is_assigned', 'workshop', 'active_recipe', 'country_id']