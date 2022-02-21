from django.db import models
from django.urls import reverse

# Create your models here.
class Trips(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.name

class Stop(models.Model):
    city = models.CharField(max_length=50)
    arrival = models.DateField('Arrival Date')
    departure = models.DateField('Departure Date')
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('stop_detail', kwargs={'stop_id': self.id})

    def __str__(self):
        return self.city

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Reservation Date')
    time = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TravelTo(models.Model):
    mode = models.CharField(max_length=50)
    date = models.DateField('Travel Date')
    departure_time = models.CharField(max_length=50)
    arrival_time = models.CharField(max_length=50)

    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)

    def __str__(self):
        return self.mode
