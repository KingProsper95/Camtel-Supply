from django.shortcuts import render
from rest_framework import generics
from CamtelSupplyAPI.models import OrderDetails
from CamtelSupplyAPI.serializers.orderDetailsSerializer import OrderDetailSerializer

class OrderDetailsView(generics.ListCreateAPIView):
    queryset = OrderDetails.objects.select_related('product','order').all()
    serializer_class = OrderDetailSerializer

class SingleOrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetails.objects.select_related('product','order').all()
    serializer_class = OrderDetailSerializer