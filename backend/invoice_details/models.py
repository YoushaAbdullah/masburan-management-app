# Create your models here.
from django.db import models
from project.models import Project  # Assuming you have the Project model already

PERCENTAGE_CHOICES = [
    (20, '20%'),
    (30, '30%'),
    (50, '50%'),
]

class InvoiceDetails(models.Model):
    inv_no = models.CharField(max_length=50)
    po_no = models.CharField(max_length=50)
    date = models.DateField()
    project_location = models.CharField(max_length=200)
    attn_to = models.CharField(max_length=100)
    project_codename = models.CharField(max_length=100)
    payment_terms = models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    invoice_to_company_location = models.CharField(max_length=200)
    invoice_percentage = models.IntegerField(choices=PERCENTAGE_CHOICES)
    invoice_company_name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice {self.inv_no} for {self.project_codename}"
