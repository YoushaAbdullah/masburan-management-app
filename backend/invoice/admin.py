# Register your models here.
from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'item_code', 'description', 'uom', 'unit_price', 
        'quantity', 'project'
    )
    search_fields = ('item_code', 'description', 'project__project_name')
    list_filter = ('uom', 'project')
    ordering = ('-id',)
