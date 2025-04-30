from django.db import models

# Create your models here.

class Project(models.Model):
    project_code = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=50)
    project_start_date = models.DateField()
    project_complete_date = models.DateField()

    def __str__(self):
        return self.project_name
