from django.urls import include, path, re_path
from rest_framework import routers
from .Views.core_views import (
    CountryView,
    CharacterView,
    CharacterByCountryView,
    GetAllStoredGoodsView,
    ProfessionInfromationView,
)
from .Views.building_views import (
    BuildingView,
    BuildingDetailView,
    BuildingByCountryView,
)
from .Views.workshop_views import (
    WorkshopCreationView,
    WorkshopHandler,
    WorkshopListAllView,
    WorkshopListByCountryView,
    WorkshopDetailView,
    WorkshopUpgradeView,
    UpgradeListCreateView,
    WorkshopListByCountryAndCharacterView,
    RecipesInWorkshopView,
)
from .Views.employee_views import (
    HireNewEmployeeView,
    EmployeeListAllView,
    EmployeeListForWorkshopAllView,
    EmployeeListForCountryAllView,
    EmployeeListForCountryUnemployedAllView,
    GiveRecipeToEmployeeView,
)
from .Views.cart_views import (
    CartListAllView,
    CartCountryView,
    CartStorageView,
    WorkshopToCartTransferView,
    StorageToStorageTransferView,
    SetCartInMotion,
    CartsAtWorkshotView,
)
from .Views.marketplace_view import (
    StallListAllView,
    StallListByCountryView,
    StallDetailView,
    SellToStall,
)
from .Views.testView import list_shopping_cart
from .Views.homepage import Homepage

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("country/", CountryView.as_view(), name="Country"),
    path(
        "professioninformation/",
        ProfessionInfromationView.as_view(),
        name="Profession Information",
    ),
    # Characters
    path("character/", CharacterView.as_view(), name="Character"),
    path(
        "character/<int:countryID>/",
        CharacterByCountryView.as_view(),
        name="Character-Country",
    ),
    # Workshops
    path("workshops/", WorkshopHandler.as_view(), name="Workshops"),
    path("workshop/<int:pk>/", WorkshopDetailView.as_view(), name="Workshop"),
    path("upgrades/", UpgradeListCreateView.as_view(), name="Upgrades"),
    path(
        "workshops/country/<int:countryID>/",
        WorkshopListByCountryView.as_view(),
        name="Workshop",
    ),
    path(
        "workshops/character/<int:characterID>/",
        WorkshopListByCountryAndCharacterView.as_view(),
        name="Workshop",
    ),
    path("workshop/upgrade/", WorkshopUpgradeView.as_view(), name="Workshop"),
    path("workshop/hire/", HireNewEmployeeView.as_view(), name="Workshop"),
    path("workshop/give-recipe/", GiveRecipeToEmployeeView.as_view(), name="Workshop"),
    path(
        "workshop/<int:workshopID>/get-recipe/",
        RecipesInWorkshopView.as_view(),
        name="Workshop",
    ),
    # Employees
    path("employees/", EmployeeListAllView.as_view(), name="Employees"),
    path(
        "employees/workshop/<int:workshopID>/",
        EmployeeListForWorkshopAllView.as_view(),
        name="Employees",
    ),
    path(
        "employees/country/<int:countryID>/",
        EmployeeListForCountryAllView.as_view(),
        name="Employees",
    ),
    path(
        "employees/country/<int:countryID>/unemployed/",
        EmployeeListForCountryUnemployedAllView.as_view(),
        name="Employees",
    ),
    path("workshop/employees/", EmployeeListAllView.as_view(), name="Employees"),
    # Handle Carts
    path("carts/", CartListAllView.as_view(), name="Carts"),
    path("carts/<int:countryID>/", CartCountryView.as_view(), name="Carts"),
    path(
        "carts/workshop/<int:workshopID>/", CartsAtWorkshotView.as_view(), name="Carts"
    ),
    path("workshop/cart/transfer/", WorkshopToCartTransferView.as_view(), name="Carts"),
    path("cart/sendtolocation/", SetCartInMotion.as_view(), name="Cart"),
    path("carts/storage/", CartStorageView.as_view(), name="CartStorage"),
    # Handle storage
    path("movetostorage/", StorageToStorageTransferView.as_view(), name="Storage"),
    path(
        "goodsinstorage/<int:storageID>/",
        GetAllStoredGoodsView.as_view(),
        name="Storage",
    ),
    # Marketplace Storage
    path("marketplace/stalls/", StallListAllView.as_view(), name="Stalls"),
    path(
        "marketplace/stalls/<int:countryID>/",
        StallListByCountryView.as_view(),
        name="Stalls",
    ),
    path("marketplace/stall/", StallDetailView.as_view(), name="Stalls"),
    path("marketplace/selltostall/", SellToStall.as_view(), name="Stalls"),
    path("buildings/", BuildingView.as_view(), name="Building"),
    path("building/", BuildingDetailView.as_view(), name="Building"),
    path(
        "buildings/<int:countryID>/", BuildingByCountryView.as_view(), name="Building"
    ),
    path("home/", Homepage, name="home"),
    path("test/", list_shopping_cart, name="home"),
]
