from django.shortcuts import render, redirect
from .models import Stop, Trips
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RestaurantForm, TravelToForm, HotelForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

### TRIP VIEWS ###

def index(request):
    trips = Trips.objects.all()
    return render(request, 'trips/index.html', {'trips': trips})

class TripsCreate(CreateView):
    model = Trips
    fields = '__all__'

class TripsUpdate(UpdateView):
  model = Trips
  fields = '__all__'

class TripsDelete(DeleteView):
  model = Trips
  success_url = '/trips/'

### STOP VIEWS ###

def stops_index(request, trip_id):
    stops = Stop.objects.filter(trip_id=trip_id)
    return render(request, 'trips/stops_index.html', {'stops': stops})

def stop_detail(request, stop_id):
    stop = Stop.objects.get(id=stop_id)
    restaurant_form = RestaurantForm()
    travelto_form = TravelToForm()
    hotel_form = HotelForm()
    return render(request, 'trips/stop_detail.html', {'stop': stop, 'restaurant_form': restaurant_form, 'travelto_form': travelto_form, 'hotel_form': hotel_form})

class StopCreate(CreateView):
    model = Stop
    fields = '__all__'

class StopUpdate(UpdateView):
    model = Stop
    fields = '__all__'

class StopDelete(DeleteView):
    model = Stop
    success_url = '/trips/'
    

### RESTAURANT VIEWS ###

def add_restaurant(request, stop_id):
  form = RestaurantForm(request.POST)
  if form.is_valid():
    new_restaurant = form.save(commit=False)
    new_restaurant.stop_id = stop_id
    new_restaurant.save()
  return redirect('stop_detail', stop_id=stop_id)

def add_travelto(request, stop_id):
  form = TravelToForm(request.POST)
  if form.is_valid():
    new_travelto = form.save(commit=False)
    new_travelto.stop_id = stop_id
    new_travelto.save()
  return redirect('stop_detail', stop_id=stop_id)

def add_hotel(request, stop_id):
  form = HotelForm(request.POST)
  if form.is_valid():
    new_hotel = form.save(commit=False)
    new_hotel.stop_id = stop_id
    new_hotel.save()
  return redirect('stop_detail', stop_id=stop_id)