# Create your models here.
from django.db import models

UNIT_CHOICES = [
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

class ItemList(models.Model):
    material_name = models.CharField(max_length=200)
    specification = models.CharField(max_length=50,choices=SPECIFICATION_CHOICES)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES)
    unit_price = models.FloatField()
    supplier = models.CharField(max_length=200)
    contact_no_supplier = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.material_name} ({self.specification})"
