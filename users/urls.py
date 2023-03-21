from django.urls import path
from . import views

from rest_framework_simplejwt import views as jwt_view

urlpatterns = [
    path("users/", views.SongView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/login/", jwt_view.TokenObtainPairView.as_view()),
    path("refresh/", jwt_view.TokenRefreshView.as_view()),
]