from .models import  ListSong
from .serializers import ListSongSerializers

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated


class SongView(generics.ListCreateAPIView):

    serializer_class = ListSongSerializers
    queryset = ListSong.objects.all()     
            
    def perform_create(self, serializer):  
        
        serializer.save()
