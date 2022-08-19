from django.forms import ModelForm
from .models import Vehicle

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ["vehicle_no", "vehicle_type", "vehicle_model", "Vehicle_desc"]