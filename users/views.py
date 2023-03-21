from .models import User
from .serializers import UserSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

class SongView(generics.ListCreateAPIView):
   

    serializer_class = UserSerializer
    queryset = User.objects.all()     
            
    def perform_create(self, serializer):  
      
        serializer.save(user=self.request.user)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "account_id"
