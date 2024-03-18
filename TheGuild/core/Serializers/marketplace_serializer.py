from TheGuild.core.Models.MarketplaceModel import Stall
from rest_framework import serializers

class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = ['id', 'building', 'country_id', 'storage_id']