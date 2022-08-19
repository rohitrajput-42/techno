from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name = "home"),
    path('add_vehicle/', AddVehicle, name = "add_vehicle"),
    path('update_vehicle/<int:id>', UpdateVehicle, name = "update_vehicle"),
    path('delete_vehicle/<int:id>', DeleteVehicle, name = "delete_vehicle"),
    path('error_403/', error_403, name = "error_403"),
    path('error_404/', error_404, name = "error_404"),
    path('error_500/', error_500, name = "error_500"),
]