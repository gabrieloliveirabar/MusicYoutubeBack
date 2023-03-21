from django.urls import path
from . import views


urlpatterns = [
    path("songs/", views.SongView.as_view()),
    path("songs/<str:pk>/", views.SongDetailView.as_view()),
]