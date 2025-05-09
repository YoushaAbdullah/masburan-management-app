from django.db import models
from project.models import Project 
from invoice_details.models import InvoiceDetails  

UOM_CHOICES = [
    ('each', 'EA'),
    ('m', 'M')
]

class Invoice(models.Model):
    item_code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    uom = models.CharField(max_length=50, choices=UOM_CHOICES)
    unit_price = models.FloatField()
    quantity = models.FloatField()
    invoice_details = models.ForeignKey(
        InvoiceDetails,
        on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice {self.item_code} for {self.project.project_name}"
