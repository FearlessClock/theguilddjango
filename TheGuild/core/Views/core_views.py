from django.shortcuts import render
from rest_framework import generics
from ..Models.CountryModel import Country
from ..Models.CharacterModel import Character
from ..Serializers.core_serializer import CountrySerializer, CharacterSerializer
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse


class CountryView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

class CharacterView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(user=user.id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]
    
class CharacterByCountryView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        filter = self.kwargs['countryID']
        if filter is not None:
            queryset = Character.objects.filter(country=filter, user=user.id)
            return queryset     
        return None