from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from TheGuild.core.Serializers.EmployeeSerializer import EmployeeSerializer
from TheGuild.core.Models.EmployeeModel import Employee
from TheGuild.core.Models.CharacterModel import Character
from TheGuild.core.Models.WorkshopModel import Workshop
from TheGuild.core.Models.GoodsModel import Recipe
from TheGuild.core.Models.CountryModel import Country

from TheGuild.core.GameManager import TickCountry


class EmployeeListAllView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class HireNewEmployeeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):    # Hire a new employee
        workshop = Workshop.objects.get(id=request.data["workshopID"])
        #TODO: Create new employee if none are waiting
        employee = Employee.objects.filter(is_assigned=False).first()
        employee.is_assigned = True
        employee.workshop = workshop
        employee.active_recipe = None
        employee.save()
        return Response('Employee ' + str(employee.id) + " hired", status=status.HTTP_200_OK)
    
    def delete(self, request):  # Fire an employee
        employee = Employee.objects.get(id=request.data["employeeID"])
        employee.is_assigned = False
        employee.workshop = None
        employee.save()
        return Response('Employee ' + str(employee.id) + " fired", status=status.HTTP_200_OK)    

class EmployeeListForWorkshopAllView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        filter = self.kwargs['workshopID']
        if filter is not None:
            queryset = Workshop.objects.filter(id=filter)
            employees = Employee.objects.filter(workshop_id__in=queryset)
            return employees
        return None
    
class EmployeeListForCountryAllView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        TickCountry(self.kwargs['countryID'])
        filter = self.kwargs['countryID']
        if filter is not None:
            employees = Employee.objects.filter(country_id=filter)
            return employees
        return None
    
class EmployeeListForCountryUnemployedAllView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        filter = self.kwargs['countryID']
        if filter is not None:
            employees = Employee.objects.filter(country_id=filter, is_assigned=False)
            return employees
        return None
    
class GiveRecipeToEmployeeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):    
        employee = Employee.objects.get(id=request.data["employeeID"])
        recipeID = request.data["recipeID"]
        recipe = Recipe.objects.get(id=recipeID)
        employee.active_recipe = recipe
        employee.save()
        return Response('Employee ' + str(employee.id) + " recipe changed to " + str(recipeID), status=status.HTTP_200_OK)
    
    def delete(self, request):
        employee = Employee.objects.get(id=request.data["employeeID"])
        employee.active_recipe = None
        employee.save()
        return Response('Employee ' + str(employee.id) + " stopped working")
        
