from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            "id", "material_name", "specification", "unit", "quantity_ordered", 
            "quantity_ordered_unit_price", "quantity_stock", "quantity_stock_unit_price", 
            "quantity_stock_acquired_site_name", "supplier", "contact_no_supplier", 
            "delivery_method", "delivery_details", "project"
        ]
        extra_kwargs = {
            "project": {"read_only": True}
        }
