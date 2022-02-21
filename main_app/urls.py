from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('trips/', views.index, name='index'),
    path('trips/create/', views.TripsCreate.as_view(), name='trips_create'),
    path('trips/<int:pk>/update/', views.TripsUpdate.as_view(), name='trips_update'),
    path('trips/<int:pk>/delete/', views.TripsDelete.as_view(), name='trips_delete'),
    path('trips/<int:trip_id>/stops/', views.stops_index, name='stops_index'),
    path('stops/<int:stop_id>/', views.stop_detail, name='stop_detail'),
    path('stops/create/', views.StopCreate.as_view(), name='stop_create'),
    path('stops/<int:pk>/update/', views.StopUpdate.as_view(), name='stop_update'),
    path('stops/<int:pk>/delete/', views.StopDelete.as_view(), name='stop_delete'),
    path('stops/<int:stop_id>/add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('stops/<int:stop_id>/add_travelto/', views.add_travelto, name='add_travelto'),
    path('stops/<int:stop_id>/add_hotel/', views.add_hotel, name='add_hotel'),
]


