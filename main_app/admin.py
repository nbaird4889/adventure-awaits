from django.contrib import admin
from .models import Restaurant, Trips, Stop, TravelTo, TravelFrom, Activity, Hotel
from .models import Stop

# Register your models here.
admin.site.register(Trips)
admin.site.register(Stop)
admin.site.register(Restaurant)
admin.site.register(TravelTo)
admin.site.register(TravelFrom)
admin.site.register(Activity)
admin.site.register(Hotel)
