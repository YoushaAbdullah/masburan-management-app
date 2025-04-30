# Register your models here.
from django.contrib import admin
from .models import DeliveryOrderDetails

@admin.register(DeliveryOrderDetails)
class DeliveryOrderDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'do_no', 'po_no', 'date', 'project_location', 'attn_to', 
        'project_codename', 'delivery_company_name', 'delivery_order_percentage', 'project'
    )
    search_fields = ('project_location', 'project', 'delivery_company_name')
    list_filter = ('date', 'delivery_order_percentage')
    ordering = ('-date',)
