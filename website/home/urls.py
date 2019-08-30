from django.contrib import admin
from django.urls import path, include

from home import views
from .views import home


urlpatterns = [
    path('', views.home, name='home-home'),

]