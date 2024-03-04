from django.urls import include, path
from rest_framework import routers
from .Views.views import CountryView, CharacterView, CharacterByCountryView
from .Views.WorkshopViews import WorkshopListAllView, WorkshopListByCountryView, WorkshopDetailView

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
    path("workshops/<int:countryID>", WorkshopListByCountryView.as_view(), name="Workshop"),
]
