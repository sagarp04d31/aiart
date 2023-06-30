from django import forms
from .models import ArtPiece

class ArtPieceForm(forms.ModelForm):
    class Meta:
        model = ArtPiece
        fields = ['image', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'm-2'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
