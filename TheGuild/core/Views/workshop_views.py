from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from TheGuild.core.Models.CountryModel import Country
from TheGuild.core.Models.CharacterModel import Character
from TheGuild.core.Models.EmployeeModel import Employee
from TheGuild.core.Models.WorkshopModel import Workshop, Upgrade, Workshop_Upgrade
from TheGuild.core.Serializers.core_serializer import CountrySerialzer, CharacterSerialzer
from TheGuild.core.Serializers.WorkshopSerializer import WorkshopSerializer, UpgradeSerializer
from TheGuild.core.Serializers.EmployeeSerializer import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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
            chars = Character.objects.filter(country_id=filter, user_id=user.id).values_list('id',  flat=True)
            queryset = Workshop.objects.filter(id__in=chars)
            return queryset
        return None
    
class WorkshopDetailView(generics.RetrieveUpdateAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [IsAuthenticated]
    
class WorkshopUpgradeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        workshopID = request.data["workshopID"]
        upgradeId = request.data["upgradeID"]
        user = self.request.user
        
        workshop = Workshop.objects.filter(id=workshopID)
        if not workshop:
            return Response('Could not find workshop with id ' + str(workshopID), status=status.HTTP_404_NOT_FOUND)
        upgrade = Upgrade.objects.filter(id=upgradeId)
        if not upgrade:
            return Response('Could not find upgrade with id ' + str(upgradeId), status=status.HTTP_404_NOT_FOUND)
        
        newUpgrade = Workshop_Upgrade(
            workshop = workshop,
            upgrade = upgrade,
            level = 0
        )
        newUpgrade.save()
        return Response('Upgrade added', status=status.HTTP_200_OK)
    
class UpgradeListCreateView(generics.ListCreateAPIView):
    queryset = Upgrade.objects.all()
    serializer_class = UpgradeSerializer