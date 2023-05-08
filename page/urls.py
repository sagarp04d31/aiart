from django.urls import path
from page.views import *

urlpatterns = [
    path("", index, name="home"),
]

