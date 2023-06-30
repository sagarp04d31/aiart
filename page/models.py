from django.db import models
from django.contrib.auth.models import User

class ArtPiece(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="uploaded_art")
    image = models.ImageField(upload_to='image/')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name="liked_art")

    def __str__(self):
        return self.description

