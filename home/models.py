from django.db import models


from django.contrib.auth.models import User
# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField(max_length=100)
    arrival_time = models.TimeField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return "%s Train" % self.name

class Seat(models.Model):
    seat_id = models.CharField(max_length=100)
    train = models.ForeignKey(Train,on_delete =models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateField()
  
    def __str__(self):
        return "%s's " % self.train.name + self.seat_id

class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pnr = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    # train = models.ForeignKey(Train,on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return "%s's Ticket" % self.user

class Search(models.Model):

    to=models.CharField(max_length=100)
    fro=models.CharField(max_length=100)

    class Meta:
     = _("Search")
        verbos = _("Searchs")

    def __str__(self):
        return self.name
)