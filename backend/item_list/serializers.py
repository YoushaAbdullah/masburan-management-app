from rest_framework import serializers
from .models import ItemList

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ['id', 'material_name', 'specification', 'unit', 'unit_price', 'supplier', 'contact_no_supplier']
