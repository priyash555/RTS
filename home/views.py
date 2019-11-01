from django.shortcuts import render
from .models import Train, Ticket
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import ticket


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
        date = request.POST.get('date',None)
        print(source)
        print(destination)
        print(date)
        trains=[]
        ptrains = (Train.objects.filter(source__iexact=source))
        for i in ptrains:
            print(i.destination.upper())
            if(i.destination.upper() == destination.upper()):
                trains.append(i)

        context={'trains':trains}
        html = render_to_string('home/trains.html',context,request=request)
        return JsonResponse({'form': html})

def ticketbook(request,id):
    train = Train.objects.filter(id=id).first()
    return render(request,'home/book.html',{'train':train})

def ticketbk(request,id):
    print("aayay habhah")    
    form = ticket()
    return render(request,'home/tick.html',{'form':form})

def realbook(request,id):
    if request.method == 'POST':
        user=request.user
        train = Train.objects.filter(id=id).first()
        date = request.POST.get('date',None)
        tcount = Ticket.objects.filter(date=date)
        g=0
        for i in tcount:
                if i.train == train:
                        g=g+1
        if(g>60):
                status = "Waiting List"
        # return render(request,'home/starting.html')
        else:
                status = "Confirm"
        o = str(date)
        p = o[0:4]
        p = p + o[5:7]
        p = p + o[8:11]
        z = Ticket.objects.all()
        po = z.count()
        po = str(po)
        print(po)
        pnr = str(train.id)+p+str(user.id)+po
        
        passenger_name = request.POST.get('name',None)
        age = request.POST.get('age',None)
        ticket = Ticket(user=user,
        pnr=pnr,status=status,date=date,train=train,passenger_name=passenger_name,
        age=age
        )
        ticket.save()
        print(passenger_name)
        return render(request,'home/starting.html')