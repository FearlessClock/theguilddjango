from django.shortcuts import render
from rest_framework import generics
from ..Models.MarketplaceModel import Stall
from ..Models.CharacterModel import Character
from ..Serializers.marketplace_serializer import StallSerializer
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

class StallListAllView(generics.ListCreateAPIView):
    queryset = Stall.objects.all()
    serializer_class = StallSerializer
    
class StallListByCountryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StallSerializer
    
    def get_queryset(self):
        filter = self.kwargs['countryID']
        if filter is not None:
            queryset = Stall.objects.filter(country_id=filter)
            return queryset
        return None
    
class StallDetailView(generics.RetrieveUpdateAPIView):
    queryset = Stall.objects.all()
    serializer_class = StallSerializer
    permission_classes = [IsAuthenticated]
    
