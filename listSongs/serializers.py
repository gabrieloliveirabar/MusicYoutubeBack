from rest_framework import serializers
from .models import ListSong

class ListSongSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListSong
        fields = [
            "id",
            
        ]