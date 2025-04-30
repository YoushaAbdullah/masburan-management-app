from django.db import models
from project.models import Project  

class Boq(models.Model):
    mm_no = models.FloatField()
    job_description = models.CharField(max_length=200)
    uom = models.CharField(max_length=150)
    unit_rate = models.FloatField()
    quantity = models.FloatField()
    boq_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='boqs')

    def __str__(self):
        return f"{self.job_description} ({self.project.project_name})"
