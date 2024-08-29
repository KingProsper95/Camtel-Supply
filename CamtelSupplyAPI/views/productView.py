from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from CamtelSupplyAPI.models  import Product
from CamtelSupplyAPI.serializers.productSerializer import ProductSerializer

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

class SingleProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

