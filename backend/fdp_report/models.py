# from django.db import models
# from project.models import Project
# from imagefield.fields import ImageField

# # Create your models here.


# class FdpReport(models.Model):
#     fdp = models.IntegerField()
#     fdc = models.IntegerField()
#     meter_reading = models.FloatField()
#     fdp_image = ImageField(
#         upload_to='fdp_images',
#         formats={
#             "thumb": ["default", ("crop", (300, 300))],
#             "desktop": ["default", ("thumbnail", (800, 600))],
#         },
#         auto_add_fields=True,  # Automatically adds width, height, and PPOI fields
#     )
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"FdpReport for Project: {self.project}"

#     class Meta:
#         verbose_name = "FDP Report"
#         verbose_name_plural = "FDP Reports"