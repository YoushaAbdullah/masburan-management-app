from rest_framework import serializers
from .models import InvoiceDetails

class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = [
            'id', 'inv_no', 'po_no', 'date', 'project_location', 'attn_to', 'project_codename',
            'payment_terms', 'account', 'project', 
            'invoice_to_company_location', 'invoice_percentage', 'invoice_company_name'
        ]
        extra_kwargs = {
            'project': {'read_only': False}
        }
