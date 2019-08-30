from django.shortcuts import render, redirect

def start(request):
    return render(request, 'home/starting.html', {})