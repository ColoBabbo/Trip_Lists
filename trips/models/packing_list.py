from django.db import models
from .trip import Trip

class Packing_List(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)