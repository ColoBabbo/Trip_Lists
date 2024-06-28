from django.db import models
from .packing_list import Packing_List

class Item(models.Model):
    packing_list = models.ForeignKey(Packing_List, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    quantity = models.FloatField(max_length=45)
    unit = models.CharField(max_length=45)
    # notes = models.CharField(max_length=255)