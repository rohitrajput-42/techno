from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

vehicle_choices = (
    ("Two", "Two"),
    ("Three", "Three"),
    ("Four", "Four"),
)

class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length = 15000)
    vehicle_type = models.CharField(max_length = 1500, choices = vehicle_choices)
    vehicle_model = models.CharField(max_length = 15000)
    Vehicle_desc = models.TextField()
    created_ts = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    updated_ts = models.DateTimeField(auto_now = True, null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.vehicle_no
