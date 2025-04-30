from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ItemList

@admin.register(ItemList)
class ItemListAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'material_name', 'specification', 'unit', 'unit_price', 
        'supplier', 'contact_no_supplier'
    )
    search_fields = ('material_name', 'specification', 'supplier', 'project__project_name')
    list_filter = ('unit', 'material_name')
    ordering = ('-id',)
