from django.contrib import admin
from django.urls import path, include
from .views import starting,trains


urlpatterns = [
    path('', starting, name="home-home"),
    path('trains/',trains,name="home-trains")
]