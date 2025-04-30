from rest_framework import serializers
from .models import Boq

class BoqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boq
        fields = [
            "id", "mm_no", "job_description", "uom", 
            "unit_rate", "quantity", "boq_date", "project"
        ]
        extra_kwargs = {
            "project": {"read_only": True}
        }
