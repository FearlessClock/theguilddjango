from TheGuild.core.Models.MarketplaceModel import Stall
from TheGuild.core.Serializers.core_serializer import BuildingSerializer
from rest_framework import serializers


class StallSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(many=False)

    class Meta:
        model = Stall
        fields = ["id", "building", "country_id", "storage_id"]
