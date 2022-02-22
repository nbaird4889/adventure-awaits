from django.shortcuts import render, redirect
from .models import Stop, Trips
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RestaurantForm, TravelFromForm, TravelToForm, HotelForm, ActivityForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, 'home.html')

### TRIP VIEWS ###

@login_required
def index(request):
    trips = Trips.objects.filter(user=request.user)
    return render(request, 'trips/index.html', {'trips': trips})

class TripsCreate(LoginRequiredMixin, CreateView):
    model = Trips
    fields = ['name', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class TripsUpdate(LoginRequiredMixin, UpdateView):
  model = Trips
  fields = '__all__'

class TripsDelete(LoginRequiredMixin, DeleteView):
  model = Trips
  success_url = '/trips/'

### STOP VIEWS ###

@login_required
def stops_index(request, trip_id):
    stops = Stop.objects.filter(trip_id=trip_id)
    return render(request, 'trips/stops_index.html', {'stops': stops})

@login_required
def stop_detail(request, stop_id):
    stop = Stop.objects.get(id=stop_id)
    restaurant_form = RestaurantForm()
    travelto_form = TravelToForm()
    hotel_form = HotelForm()
    activity_form = ActivityForm()
    travelfrom_form = TravelFromForm
    return render(request, 'trips/stop_detail.html', {'stop': stop, 'restaurant_form': restaurant_form, 'travelto_form': travelto_form, 'hotel_form': hotel_form, 'activity_form': activity_form, 'travelfrom_form': travelfrom_form})

class StopCreate(LoginRequiredMixin, CreateView):
    model = Stop
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['trip'].queryset = Trips.objects.filter(user=self.request.user)    
        return context

class StopUpdate(LoginRequiredMixin, UpdateView):
    model = Stop
    fields = '__all__'

class StopDelete(LoginRequiredMixin, DeleteView):
    model = Stop
    success_url = '/trips/'
    

### RESTAURANT VIEWS ###
@login_required
def add_restaurant(request, stop_id):
  form = RestaurantForm(request.POST)
  if form.is_valid():
    new_restaurant = form.save(commit=False)
    new_restaurant.stop_id = stop_id
    new_restaurant.save()
  return redirect('stop_detail', stop_id=stop_id)

@login_required
def add_travelto(request, stop_id):
  form = TravelToForm(request.POST)
  if form.is_valid():
    new_travelto = form.save(commit=False)
    new_travelto.stop_id = stop_id
    new_travelto.save()
  return redirect('stop_detail', stop_id=stop_id)

@login_required
def add_hotel(request, stop_id):
  form = HotelForm(request.POST)
  if form.is_valid():
    new_hotel = form.save(commit=False)
    new_hotel.stop_id = stop_id
    new_hotel.save()
  return redirect('stop_detail', stop_id=stop_id)

@login_required
def add_activity(request, stop_id):
  form = ActivityForm(request.POST)
  if form.is_valid():
    new_activity = form.save(commit=False)
    new_activity.stop_id = stop_id
    new_activity.save()
  return redirect('stop_detail', stop_id=stop_id)

@login_required
def add_travelfrom(request, stop_id):
  form = TravelFromForm(request.POST)
  if form.is_valid():
    new_travelfrom = form.save(commit=False)
    new_travelfrom.stop_id = stop_id
    new_travelfrom.save()
  return redirect('stop_detail', stop_id=stop_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up, please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)