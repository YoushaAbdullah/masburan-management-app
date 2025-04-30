# Create your models here.
from django.db import models

class ItemList(models.Model):
    material_name = models.CharField(max_length=200)
    specification = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    unit_price = models.FloatField()
    supplier = models.CharField(max_length=200)
    contact_no_supplier = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.material_name} ({self.specification})"
