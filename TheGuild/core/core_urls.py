from django.urls import include, path
from rest_framework import routers
from .Views.core_views import CountryView, CharacterView, CharacterByCountryView
from .Views.workshop_views import WorkshopListAllView, WorkshopListByCountryView, WorkshopDetailView, WorkshopUpgradeView, UpgradeListCreateView
from .Views.employee_views import HireNewEmployeeView,EmployeeListAllView, EmployeeListForWorkshopAllView, EmployeeListForCountryAllView,EmployeeListForCountryUnemployedAllView, GiveRecipeToEmployeeView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("country/", CountryView.as_view(), name='Country'),
    # Characters
    path("character/", CharacterView.as_view(), name='Character'),
    path("character/<int:countryID>/", CharacterByCountryView.as_view(), name="Character"),
    
    # Workshops
    path("workshops/", WorkshopListAllView.as_view(), name="Workshop"),
    path("workshop/", WorkshopDetailView.as_view(), name="Workshop"),
    path("upgrades/", UpgradeListCreateView.as_view(), name="Upgrades"),
    path("workshops/<int:countryID>/", WorkshopListByCountryView.as_view(), name="Workshop"),
    path("workshop/upgrade/", WorkshopUpgradeView.as_view(),name="Workshop"),
    path("workshop/hire/", HireNewEmployeeView.as_view(),name="Workshop"),
    path("workshop/give-recipe/", GiveRecipeToEmployeeView.as_view(),name="Workshop"),
    path("employees/", EmployeeListAllView.as_view(),name="Employees"),
    path("employees/workshop/<int:workshopID>/", EmployeeListForWorkshopAllView.as_view(),name="Employees"),
    path("employees/country/<int:countryID>/", EmployeeListForCountryAllView.as_view(),name="Employees"),
    path("employees/country/<int:countryID>/unemployed/", EmployeeListForCountryUnemployedAllView.as_view(),name="Employees"),
    path("workshop/employees/", EmployeeListAllView.as_view(),name="Employees")
]
