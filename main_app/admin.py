from django.contrib import admin
from .models import Restaurant, Trips, Stop, TravelTo
from .models import Stop

# Register your models here.
admin.site.register(Trips)
admin.site.register(Stop)
admin.site.register(Restaurant)
admin.site.register(TravelTo)
