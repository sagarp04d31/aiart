from django.shortcuts import render
from .models import ArtPiece

def index(request):
    arts = ArtPiece.objects.all()
    return render(request, 'page/index.html', { 'arts': arts})




