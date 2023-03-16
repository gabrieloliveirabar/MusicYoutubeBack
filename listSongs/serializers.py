from rest_framework import serializers
from .models import ListSong

class ListSongSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListSong
        fields = [
            "id",
            "buyed_at"
        ]
    def create(self, validated_data: dict) -> ListSong:
        return ListSong.objects.create()