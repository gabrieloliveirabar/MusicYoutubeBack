from .models import Song
from .serializers import SongSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
import ipdb

class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = SongSerializer
    queryset = Song.objects.all()     
            
    def perform_create(self, serializer):  
        
        serializer.save(user=self.request.user)

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = SongSerializer
    queryset = Song.objects.all()
    