from django.urls import include, path
from .account_views import UserLoginView, UserRegisterView, UserDeleteView, UserListView, LoginView, UserDetailView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("user_login/", UserLoginView.as_view()),
    path("login/", LoginView.as_view()),
    path("register/", UserRegisterView.as_view()),
    path("delete/", UserDeleteView.as_view()),
    path("users/", UserListView.as_view()),
    path("user/<int:pk>/", UserDetailView.as_view()),
]
