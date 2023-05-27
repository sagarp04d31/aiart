from django.db import models

class ArtPiece(models.Model):
    image = models.ImageField(upload_to='image')
    description = models.TextField()

    def __str__(self):
        return self.description
    
