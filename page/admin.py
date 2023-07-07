from django.contrib import admin
from .models import ArtPiece
from users.models import Profile

admin.site.register(ArtPiece)
admin.site.register(Profile)
