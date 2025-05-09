from rest_framework import serializers
from .models import DeliveryOrder

class DeliveryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOrder
        fields = [
            "id", "item_code", "description", "uom", 
            "unit_price", "quantity", "project","delivery_order_details"
        ]
        extra_kwargs = {
            "project": {"read_only": True}
        }
