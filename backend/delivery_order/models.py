from django.db import models
from project.models import Project  
from delivery_order_details.models import DeliveryOrderDetails

UOM_CHOICES = [
    ('each', 'EA'),
    ('m', 'M')
]

class DeliveryOrder(models.Model):
    item_code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    uom = models.CharField(max_length=50, choices=UOM_CHOICES)
    unit_price = models.FloatField()
    quantity = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    delivery_order_details = models.ForeignKey(
        DeliveryOrderDetails,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.item_code} - {self.project.project_name}"
