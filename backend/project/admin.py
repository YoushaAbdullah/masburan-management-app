from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_code', 'project_name', 'project_type', 'project_start_date', 'project_complete_date')
    search_fields = ('project_code', 'project_name', 'project_type')
    list_filter = ('project_type','project_name', 'project_start_date', 'project_complete_date')
    ordering = ('-project_start_date',)
