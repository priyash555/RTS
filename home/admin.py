from django.contrib import admin

# Register your models here.


from .models import Train,Seat,Ticket

admin.site.register(Train)
admin.site.register(Seat)
admin.site.register(Ticket)