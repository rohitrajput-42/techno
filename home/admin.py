from django.contrib import admin
from .models import *

class AdminVehicle(admin.ModelAdmin):
    list_display = ["id", "vehicle_no", "vehicle_type", "vehicle_model", "Vehicle_desc"]

admin.site.register(Vehicle, AdminVehicle)