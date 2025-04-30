# Register your models here.
from django.contrib import admin
from .models import DeliveryOrder

@admin.register(DeliveryOrder)
class DeliveryOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_code', 'description', 'uom', 'unit_price', 'quantity', 'project')
    search_fields = ('item_code', 'description', 'uom')
    list_filter = ('description', 'uom')
    ordering = ('description',)
