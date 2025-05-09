from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'id', 'item_code', 'description', 'uom', 'unit_price', 
            'quantity',"invoice_details", 'project'
        ]
        extra_kwargs = {
            'project': {'read_only': True}
        }
