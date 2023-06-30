
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ArtPiece
from .forms import ArtPieceForm

@login_required
def index(request):
    arts = ArtPiece.objects.all()
    size_type = ['card-tall', 'card-wide', '']
    return render(request, 'page/index.html', { 'arts': arts, 'size_type': size_type})

@login_required
def personal(request):
    current_user = request.user
    liked_arts = ArtPiece.objects.filter(likes__in=[current_user])
    return render(request, 'page/personal.html', { 'arts': liked_arts })

@login_required
def personal_upload(request):
    current_user = request.user
    arts = ArtPiece.objects.filter(user=current_user)
    return render(request, 'page/personal.html', { 'arts': arts })

@login_required
def upload(request):
    if request.method == 'POST':
        form = ArtPieceForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save(commit=False)
            art.user = request.user
            art.save()
            return redirect('home')
    else:
        form = ArtPieceForm()
        return render(request, 'page/upload.html', { 'form': form })


def test(request):
    return render(request, 'page/test.html')


def like(request, art_id):
    art = ArtPiece.objects.get(pk=art_id)
    if request.user.is_authenticated:
        if request.user in art.likes.all():
            art.likes.remove(request.user)
        else:
            art.likes.add(request.user)

def like_art(request, art_id):
    like(request, art_id)
    return redirect('personal')

def personal_like(request, art_id):
    like(request, art_id)
    return redirect('personal')


# Details
def details(request, art_id):
    art = ArtPiece.objects.get(pk=art_id)
    return render(request, 'page/details.html', { 'art': art })






