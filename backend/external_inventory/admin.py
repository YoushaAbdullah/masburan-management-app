# Register your models here.
from django.contrib import admin
from .models import ExternalInventory

@admin.register(ExternalInventory)
class ExternalInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'material_name', 'specification', 'unit', 'quantity_ordered', 
        'quantity_ordered_unit_price', 'quantity_stock', 'quantity_stock_unit_price', 
        'supplier', 'contact_no_supplier','status', 'project'
    )
    search_fields = ('material_name', 'specification', 'supplier', 'contact_no_supplier')
    list_filter = ('material_name','project')
    ordering = ('-id',)
