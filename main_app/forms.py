from django.forms import ModelForm
from .models import Restaurant, TravelTo

class RestaurantForm(ModelForm):
  class Meta:
    model = Restaurant
    fields = ['name', 'date', 'time', 'address']

class TravelToForm(ModelForm):
  class Meta:
    model = TravelTo
    fields = ['mode', 'date', 'departure_time', 'arrival_time']