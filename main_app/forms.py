from django.forms import ModelForm
from .models import Restaurant, TravelTo, Hotel, Activity, TravelFrom

class RestaurantForm(ModelForm):
  class Meta:
    model = Restaurant
    fields = ['name', 'date', 'time', 'address']

class TravelToForm(ModelForm):
  class Meta:
    model = TravelTo
    fields = ['mode', 'date', 'departure_time', 'arrival_time']

class HotelForm(ModelForm):
  class Meta:
    model = Hotel
    fields = ['name', 'address', 'confirmation_number']

class ActivityForm(ModelForm):
  class Meta:
    model = Activity
    fields = ['name', 'date', 'notes']

class TravelFromForm(ModelForm):
  class Meta:
    model = TravelFrom
    fields = ['mode', 'date', 'departure_time', 'arrival_time', 'destination']