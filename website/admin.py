from django.contrib import admin
from .models import Region, Country, State, City, LocationData


admin.site.register(Region)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(LocationData)
