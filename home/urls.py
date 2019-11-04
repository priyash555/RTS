from django.contrib import admin
from django.urls import path, include
from .views import starting,trains,ticketbook,ticketbk,realbook,ticket,tickt,canceltic,pnrstatus,about,payment


urlpatterns = [
    path('', starting, name="home-home"),
    path('about/', about, name="about"),
    path('trains/',trains,name="home-trains"),
    path('book/<int:id>/',ticketbook,name="home-book"),
    path('book/<int:id>/form/',ticketbk,name="home-bookform"),
    path('tickbk/',ticketbk,name="home-bk"),
    path('book/<int:id>/form/realbook/',realbook,name="home-realbook"),
    path('ticket/<str:pnr>/',tickt,name="tickt"),
    path('canceltic/<str:pnr>/',canceltic,name="home-cantic"),
    path('pnrstatus',pnrstatus,name="pnrstatus"),
    path('payment/', payment, name='payment'),
]