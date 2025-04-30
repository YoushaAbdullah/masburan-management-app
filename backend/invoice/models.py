from django.db import models

# Create your models here.
from django.db import models
from project.models import Project  # Assuming the Project model is already present

class Invoice(models.Model):
    item_code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    uom = models.CharField(max_length=50)
    unit_price = models.FloatField()
    quantity = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='invoices')

    def __str__(self):
        return f"Invoice {self.item_code} for {self.project.project_name}"
