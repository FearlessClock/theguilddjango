from django.shortcuts import render
from rest_framework import generics
from ..Models.BuildingModel import Building
from ..Models.CharacterModel import Character
from ..Serializers.core_serializer import (
    CountrySerializer,
    CharacterSerializer,
    BuildingSerializer,
)
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse


class BuildingView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]


class BuildingDetailView(generics.RetrieveUpdateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]


class BuildingByCountryView(generics.ListAPIView):
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filter = self.kwargs["countryID"]
        if filter is not None:
            return Building.objects.filter(country_id=filter)
        return None
