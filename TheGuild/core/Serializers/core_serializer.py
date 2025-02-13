from django.contrib.auth.models import Group, User
from rest_framework import serializers
from ..Models.CountryModel import Country, GridPoint
from ..Models.CharacterModel import Character
from ..Models.BuildingModel import Building
from ..Models.ProfessionInformationModel import ProfessionInformation


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name", "tick", "last_update", "start_date", "tick_in_seconds"]


class CharacterSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Character
        fields = ["id", "country", "user", "firstName", "familyName", "money"]


class GridPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GridPoint
        fields = ["id", "country", "x", "y", "has_building"]


class BuildingSerializer(serializers.ModelSerializer):
    grid_point = GridPointSerializer(many=False)

    class Meta:
        model = Building
        fields = ["id", "country", "grid_point", "type", "name"]


class ProfessionInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionInformation
        fields = ["id", "name", "description"]
