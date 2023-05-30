from django.shortcuts import render
from .models import ArtPiece

def index(request):
    arts = ArtPiece.objects.all()
    return render(request, 'page/index.html', { 'arts': arts})

def test(request):
    return render(request, 'page/test.html')


