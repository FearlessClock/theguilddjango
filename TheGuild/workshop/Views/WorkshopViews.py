from django.shortcuts import render
from rest_framework import generics
from TheGuild.workshop.Models.CountryModel import Country
from TheGuild.workshop.Models.CharacterModel import Character
from TheGuild.workshop.Models.WorkshopModel import Workshop, Upgrade
from TheGuild.workshop.Serializers.serializer import CountrySerialzer, CharacterSerialzer
from TheGuild.workshop.Serializers.WorkshopSerializer import WorkshopSerializer, UpgradeSerializer
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse


class WorkshopListAllView(generics.ListCreateAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    
class WorkshopListByCountryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkshopSerializer
    
    def get_queryset(self):
        user = self.request.user
        filter = self.kwargs['countryID']
        if filter is not None:
            chars = Character.objects.filter(country_id=filter, user_id=user.id)
            #queryset = Workshop.objects.filter(character_id=chars, user_id=user.id)
            return chars
        return None
    
class WorkshopDetailView(generics.RetrieveUpdateAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [IsAuthenticated]
        

class CharacterView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(user_id=user.id)
    serializer_class = CharacterSerialzer
    permission_classes = [IsAuthenticated]
    
class CharacterByCountryView(generics.ListAPIView):
    serializer_class = CharacterSerialzer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        filter = self.kwargs['countryID']
        if filter is not None:
            queryset = Character.objects.filter(country_id=filter, user_id=user.id)
            return queryset     
        return None