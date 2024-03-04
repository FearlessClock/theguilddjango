from django.urls import include, path
from .views import UserLoginView, UserRegisterView, UserDeleteView, UserListView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("login/", UserLoginView.as_view()),
    path("register/", UserRegisterView.as_view()),
    path("delete/", UserDeleteView.as_view()),
    path("users/", UserListView.as_view()),
]
