from django.db import models
from project.models import Project  

PERCENTAGE_CHOICES = [
    (20, '20%'),
    (30, '30%'),
    (50, '50%'),
]

class DeliveryOrderDetails(models.Model):
    do_no = models.CharField(max_length=50)
    po_no = models.CharField(max_length=50)
    date = models.DateField()
    project_location = models.CharField(max_length=200)
    attn_to = models.CharField(max_length=100)
    project_codename = models.CharField(max_length=100)
    declaration = models.CharField(max_length=200)
    delivery_location = models.CharField(max_length=200)
    delivery_order_percentage = models.IntegerField(choices=PERCENTAGE_CHOICES)
    delivery_company_name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"DO No: {self.do_no} - Project: {self.project_codename}"
