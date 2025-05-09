# Create your models here.
from django.db import models
from project.models import Project 


DELIVERY_METHOD_CHOICES = [
        ('delivery to site', 'Delivery to site'),
        ('pick up', 'Pick Up'),
        ('external w house', 'External Warehouse'),
    ]
UNIT_METHOD_CHOICES = [
        ('each', 'Each'),
        ('m', 'M'),
        ('roll', 'Roll'),
        ('lgth (6m)', 'Length(6m)'),
        ('coil', 'Coil'),
        ('set', 'Set'),
    ]
SPECIFICATION_CHOICES = [
        ('manhole', 'Manhole'),
        ('manhole accessories', 'Manhole Accessories'),
        ('fiber accessories', 'Fiber Accessories'),
        ('cable', 'Cable'),
        ('pipe & ducting', 'Pipe & Ducting'),
        ('pole', 'Pole'),
        ('pole accessories', 'Pole Accessories'),
        ('miscellaneous', 'Miscellaneous'),
    ]

class ExternalInventory(models.Model):
    material_name = models.CharField(max_length=200)
    specification = models.CharField(max_length=50, choices=SPECIFICATION_CHOICES)
    unit = models.CharField(max_length=50, choices=UNIT_METHOD_CHOICES)
    quantity_ordered = models.IntegerField()
    quantity_ordered_unit_price = models.FloatField()
    quantity_stock = models.IntegerField()
    quantity_stock_unit_price = models.FloatField()
    quantity_stock_acquired_from_site_name = models.CharField(max_length=250)
    supplier = models.CharField(max_length=200)
    contact_no_supplier = models.CharField(max_length=50)
    delivery_method = models.CharField(max_length=50, choices=DELIVERY_METHOD_CHOICES)
    delivery_details = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.material_name} ({self.specification})"
