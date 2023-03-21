from django.db import models
import uuid

class Song(models.Model):
    
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    link = models.CharField(max_length=600)
    user= models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="songs"
    )