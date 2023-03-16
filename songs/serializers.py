from rest_framework import serializers
from .models import Song

import ipdb

from pytube import YouTube
import moviepy.editor as mp

import os
import re

class SongSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Song
        fields = [
            "id",
            "link",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Song:
              
          link = self.data["link"]
          path = "Downloads"
         
          yt = YouTube(link)
          ys = yt.streams.filter(only_audio=True).first().download(path)
          
          for file in os.listdir(path):
            if re.search("mp4", file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0]+".mp3")
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
               
            return Song.objects.create(**validated_data)
