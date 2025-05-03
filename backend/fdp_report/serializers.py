# from rest_framework import serializers
# from .models import FdpReport
# from project.models import Project

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ('id', 'project_name')

# class FdpReportSerializer(serializers.ModelSerializer):
#     project = ProjectSerializer()

#     class Meta:
#         model = FdpReport
#         fields = ('fdp', 'fdc', 'meter_reading', 'image', 'project')
