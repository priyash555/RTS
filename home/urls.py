from django.contrib import admin
from django.urls import path, include
from .views import starting


urlpatterns = [
    path('', starting, name="home-home"),
]