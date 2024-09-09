from rest_framework import serializers
from CamtelSupplyAPI.models import Entity

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ['id', 'name']