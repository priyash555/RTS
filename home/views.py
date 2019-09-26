from django.shortcuts import render
from .models import Train
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.
def starting(request):
    user=request.user
    print("jdcncj")
    return render(request,'home/starting.html',{'user':user})

def trains(request):
    
    if request.is_ajax():
        print("aaya")
        source = request.POST.get('source',None)
        destination = request.POST.get('destination',None)
        print(source)
        print(destination)
        trains=[]
        ptrains = (Train.objects.filter(source=source))
        for i in ptrains:
            if(i.destination == destination):
                trains.append(i)

        context={'trains':trains}
        html = render_to_string('home/trains.html',context,request=request)
        return JsonResponse({'form': html})
