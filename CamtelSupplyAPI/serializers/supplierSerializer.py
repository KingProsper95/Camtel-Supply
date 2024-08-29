from rest_framework import serializers
from CamtelSupplyAPI.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'number', 'created_at']

