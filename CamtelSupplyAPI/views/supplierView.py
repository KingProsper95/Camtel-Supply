from rest_framework import generics
from CamtelSupplyAPI.models import Supplier
from CamtelSupplyAPI.serializers.supplierSerializer import SupplierSerializer

class SupplierView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SingleSupplierView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer