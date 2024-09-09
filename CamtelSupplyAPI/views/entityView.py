from django.shortcuts import render
from rest_framework import generics
from CamtelSupplyAPI.models import Entity
from CamtelSupplyAPI.serializers.entitySerializer import EntitySerializer

class EntityView(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class SingleEntityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

