from .models import Song
from .serializers import SongSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated


class SongView(generics.ListCreateAPIView):
   

    serializer_class = SongSerializer
    queryset = Song.objects.all()     
            
    def perform_create(self, serializer):  
      
        serializer.save()
