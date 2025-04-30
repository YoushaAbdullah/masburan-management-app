# Create your models here.
from django.db import models
from project.models import Project 

class BesterInventory(models.Model):
    material_name = models.CharField(max_length=200)
    specification = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    quantity_ordered = models.IntegerField()
    quantity_ordered_unit_price = models.FloatField()
    quantity_stock = models.IntegerField()
    quantity_stock_unit_price = models.FloatField()
    quantity_stock_acquired_from_site_name = models.CharField(max_length=250)
    supplier = models.CharField(max_length=200)
    contact_no_supplier = models.CharField(max_length=50)
    delivery_method = models.CharField(max_length=50)
    delivery_details = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bester_inventories')

    def __str__(self):
        return f"{self.material_name} ({self.specification})"
