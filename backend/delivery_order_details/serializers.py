from rest_framework import serializers
from .models import DeliveryOrderDetails

class DeliveryOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOrderDetails
        fields = [
            "id", "do_no", "po_no", "date", "project_location", "attn_to", 
            "project_codename", "declaration", "delivery_location", 
            "delivery_company_name", "project", "delivery_order_percentage"
        ]
        extra_kwargs = {
            "project": {"read_only": True},
            "delivery_order_percentage": {"read_only": True}
        }
