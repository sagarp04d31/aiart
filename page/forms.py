from django import forms
from .models import ArtPiece

class ArtPieceForm(forms.ModelForm):
    class Meta:
        model = ArtPiece
        fields = ['image', 'title', 'description']


