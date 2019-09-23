from django.shortcuts import render

# Create your views here.
def starting(request):
    return render(request,'home/starting.html',{})