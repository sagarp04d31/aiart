
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ArtPiece
from .forms import ArtPieceForm
from users.models import Profile

@login_required
def index(request):
    arts = ArtPiece.objects.all()
    size_type = ['card-tall', 'card-wide', '']
    return render(request, 'page/index.html', { 'arts': arts, 'card': size_type})

# Personal
@login_required
def personal_like(request):
    current_user = request.user
    liked_arts = ArtPiece.objects.filter(likes__in=[current_user])
    return render(request, 'page/personal.html', { 'arts': liked_arts, 'user': current_user })

@login_required
def personal_upload(request):
    current_user = request.user
    arts = ArtPiece.objects.filter(user=current_user)
    return render(request, 'page/personal.html', { 'arts': arts })

@login_required
def personal_following(request):
    profile = Profile.objects.all()
    return render(request, 'page/personal.html')

# Follow
@login_required
def follow(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.user.is_authenticated:
        if request.user in user.profile.followers.all():
            user.profile.followers.remove(request.user)
        else:
            user.profile.followers.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# Upload
@login_required
def upload(request):
    if request.method == 'POST':
        form = ArtPieceForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save(commit=False)
            art.user = request.user
            art.save()
            return redirect('personal_upload')
    else:
        form = ArtPieceForm()
        return render(request, 'page/upload.html', { 'form': form })


def test(request):
    return render(request, 'page/test.html')

@login_required
def like_art(request, art_id):
    art = ArtPiece.objects.get(pk=art_id)
    if request.user.is_authenticated:
        if request.user in art.likes.all():
            art.likes.remove(request.user)
        else:
            art.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# Details
@login_required
def details(request, art_id):
    art = ArtPiece.objects.get(pk=art_id)
    return render(request, 'page/details.html', { 'art': art })

# Edit
@login_required
def edit(request, art_id):
    art = ArtPiece.objects.get(pk=art_id)
    if request.method == 'POST':
        form = ArtPieceForm(request.POST, request.FILES, instance=art)
        if form.is_valid():
            art = form.save(commit=False)
            art.user = request.user
            art.save()
            return redirect('/personal/upload')
    else:
        form = ArtPieceForm(instance=art)
        return render(request, 'page/upload.html', { 'form': form })


# Delete
@login_required
def delete(request, art_id):
    art = ArtPiece.objects.get(pk=art_id)
    art.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# User
@login_required
def user(request, user_id):
    arts = ArtPiece.objects.filter(user=user_id)
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user_id)
    followers = profile.followers.all()
    following = profile.user.following.all()

    context = {
        'arts': arts,
        'followers': followers,
        'following': following,
        'follow': user,
        'is_following': request.user in followers,
    }

    return render(request, 'page/user.html', context)


# Community
## Following
@login_required
def following(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    following = profile.user.following.all()

    arts = []
    for follow in following:
        flw_user = follow.user
        art_piece = ArtPiece.objects.filter(user=flw_user)
        for art in art_piece:
            arts.append(art)

    return render(request, 'page/following.html', { 'following': following, 'arts': arts })


## Followers
@login_required
def followers(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    followers = profile.followers.all()

    return render(request, 'page/followers.html', { 'followers': followers })


# Auth Views Login
