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

from TheGuild.core.GameManagement.GameManager import TickCountry


class EmployeeListAllView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class HireNewEmployeeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):    # Hire a new employee
        workshop = Workshop.objects.get(id=request.data["workshopID"])
        #TODO: Create new employee if none are waiting
        employee = Employee.objects.filter(is_assigned=False, country=workshop.character.country).first()
        if employee:
            employee.is_assigned = True
            employee.workshop = workshop
            employee.active_recipe = None
            employee.save()
            return Response({'success':True, 'employee':employee.id}, status=status.HTTP_200_OK)
        else:
            return Response({'success':False, 'message':"No available employee found"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):  # Fire an employee
        try:
            employee = Employee.objects.get(id=request.data["employeeID"])
            employee.is_assigned = False
            employee.workshop = None
            employee.save()
            return Response({'success':True, 'employee':employee.id}, status=status.HTTP_200_OK)    
        except:
            return Response({'success':False, 'message':"Employee not found"}, status=status.HTTP_400_BAD_REQUEST)    

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
        employeeID = request.data["employeeID"]
        recipeID = request.data["recipeID"]
        try:
            employee = Employee.objects.get(id=employeeID)
        except:
            return Response({'success':False, 'employee':employeeID, 'recipeID':recipeID}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            recipe = Recipe.objects.get(id=recipeID)
        except:
            return Response({'success':False, 'employee':employee.id, 'recipeID':recipeID}, status=status.HTTP_400_BAD_REQUEST)            
        
        employee.active_recipe = recipe
        employee.save()
        return Response({'success':True, 'employee':employee.id, 'recipeID':recipeID}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        try:
            employee = Employee.objects.get(id=request.data["employeeID"])
            employee.active_recipe = None
            employee.save()
            return Response({'success':True, 'employee':employee.id}, status=status.HTTP_200_OK)
        except:
            return Response({'success':False, 'employee':employee.id}, status=status.HTTP_400_BAD_REQUEST)
        
