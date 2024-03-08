from TheGuild.core.Models.WorkshopModel import Workshop, Upgrade
from rest_framework import serializers

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['id', 'character', 'name', 'type']
        
class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgrade
        fields = ['id', 'max_level', 'name']
        
class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['id', 'character', 'name', 'type', 'upgrade', 'tick', 'last_update']