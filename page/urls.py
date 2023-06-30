from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as page_views
from users import views as user_views

urlpatterns = [
    path('', page_views.index, name='home'),
    path('personal/like', page_views.personal, name='personal'),
    path('personal/upload', page_views.personal_upload, name='personal_upload'),
    path('like/<int:art_id>', page_views.like_art, name='like_art'),
    path('personal/like/<int:art_id>', page_views.personal_like, name='personal_like'),
    path('upload', page_views.upload, name='upload'),
    path('register', user_views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('details/<int:art_id>', page_views.details, name='details'),
]




