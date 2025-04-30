from django.db import models
from project.models import Project  


class DeliveryOrder(models.Model):
    item_code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    uom = models.CharField(max_length=50)
    unit_price = models.FloatField()
    quantity = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="delivery_orders") 

    def __str__(self):
        return f"{self.item_code} - {self.project.project_name}"
