# Register your models here.
from django.contrib import admin
from .models import Boq

@admin.register(Boq)
class BoqAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_description', 'uom', 'unit_rate', 'quantity', 'boq_date', 'project')
    search_fields = ('job_description', 'project')
    list_filter = ('boq_date', 'uom', 'project')
    ordering = ('-boq_date',)
