from django.shortcuts import render
from rest_framework import generics
from CamtelSupplyAPI.models import Order
from CamtelSupplyAPI.serializers.orderSerializer import OrderSerializer

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.select_related('entity').all()
    serializer_class = OrderSerializer

class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.select_related('entity').all()
    serializer_class = OrderSerializer