from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from TheGuild.core.Models.CharacterModel import Character
from TheGuild.core.Models.WorkshopModel import (
    Workshop,
    Upgrade,
    Workshop_Upgrade,
    Workshop_Recipe,
)
from TheGuild.core.Serializers.WorkshopSerializer import (
    WorkshopSerializer,
    WorkshopCreationSerializer,
    UpgradeSerializer,
    WorkshopRecipeWithFullRecipeSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from TheGuild.core.GameManagement.GameManager import UpdateWorkshop
from django.views.generic.base import View

class WorkshopHandler(View):
    def get(self, request, *args, **kwargs):
        return WorkshopListAllView.as_view()(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return WorkshopCreationView.as_view()(request, *args, **kwargs)


class WorkshopListAllView(generics.ListAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class WorkshopCreationView(generics.CreateAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopCreationSerializer


class WorkshopListByCountryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkshopSerializer

    def get_queryset(self):
        user = self.request.user
        filter = self.kwargs["countryID"]
        if filter is not None:
            chars = Character.objects.filter(
                country_id=filter, user_id=user.id
            ).values_list("id", flat=True)
            queryset = Workshop.objects.filter(id__in=chars)
            for workshop in queryset:
                UpdateWorkshop(workshop)
            return queryset
        return None


class WorkshopListByCountryAndCharacterView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkshopSerializer

    def get_queryset(self):
        user = self.request.user
        characterID = self.kwargs["characterID"]
        if characterID is not None:
            char = Character.objects.get(id=characterID, user_id=user.id)
            queryset = Workshop.objects.filter(character_id=char.id)
            for workshop in queryset:
                UpdateWorkshop(workshop)
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
            return Response(
                "Could not find workshop with id " + str(workshopID),
                status=status.HTTP_404_NOT_FOUND,
            )
        upgrade = Upgrade.objects.filter(id=upgradeId)
        if not upgrade:
            return Response(
                "Could not find upgrade with id " + str(upgradeId),
                status=status.HTTP_404_NOT_FOUND,
            )

        newUpgrade = Workshop_Upgrade(workshop=workshop, upgrade=upgrade, level=0)
        newUpgrade.save()
        return Response("Upgrade added", status=status.HTTP_200_OK)


class UpgradeListCreateView(generics.ListCreateAPIView):
    queryset = Upgrade.objects.all()
    serializer_class = UpgradeSerializer


class RecipesInWorkshopView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkshopRecipeWithFullRecipeSerializer

    def get_queryset(self):
        workshopID = self.kwargs["workshopID"]
        return Workshop_Recipe.objects.filter(workshop_id=workshopID)
