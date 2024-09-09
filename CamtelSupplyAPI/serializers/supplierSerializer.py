from rest_framework import serializers
from CamtelSupplyAPI.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='supplier-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Supplier
        fields = ['url', 'id', 'name', 'number', 'created_at']

