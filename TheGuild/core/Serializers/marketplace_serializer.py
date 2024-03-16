from TheGuild.core.Models.MarketplaceModel import Stall
from rest_framework import serializers

class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = ['id', 'name', 'country_id', 'storage_id', 'location']