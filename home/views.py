from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehicle
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required
from home.decorators import allowed_users

@login_required
def Index(request):
    context = {}
    vehicles = Vehicle.objects.all().order_by('-created_ts')

    context["vehicles"] = vehicles
    return render(request, "index.html", context)

@login_required
@allowed_users(allowed_roles=["superadmin", ])
def AddVehicle(request):

    if request.method == "POST":
        user = request.user
        form = VehicleForm(request.POST)

        if form.is_valid():
            addv = form.save(commit = False)
            addv.user = user
            addv.save()
            return redirect("/")
    else:
        context = {}
        form = VehicleForm()
        
        context["form"] = form
        return render(request, "add_vehicle.html", context)

    return render(request, "add_vehicle.html")

@login_required
@allowed_users(allowed_roles=["superadmin", "admin"])
def UpdateVehicle(request, id):
    context = {}
    vehicle = Vehicle.objects.get(pk = id)
    form = VehicleForm(request.POST or None, instance = vehicle)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context["vehicle"] = vehicle
    context["form"] = form

    return render(request, "update_vehicle.html", context)

@login_required
@allowed_users(allowed_roles=["superadmin", ])
def DeleteVehicle(request, id):
    Vehicle.objects.get(pk=id).delete()
    return redirect("/")

@login_required
def error_403(request):
    return render(request, "403.html")

@login_required
def error_404(request, *args, **kwargs):
	return render(request, "404.html", status=404)

@login_required
def error_500(request, *args, **kwargs):
	return render(request, "500.html", status=500)