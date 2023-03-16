from django.db import models
import uuid

class ListSong(models.Model):
    
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    buyed_at = models.DateTimeField(auto_now_add=True)