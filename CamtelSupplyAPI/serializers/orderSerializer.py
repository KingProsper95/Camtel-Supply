from rest_framework import serializers
from CamtelSupplyAPI.models import Order, Entity
from CamtelSupplyAPI.serializers.entitySerializer import EntitySerializer

class OrderSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)
    client = serializers.CharField(write_only=True, max_length=255)
    url = serializers.HyperlinkedIdentityField(
        view_name='order-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Order
        fields = ['url','id','status', 'date', 'entity','client', 'created_at']

    def validate_status(self, value):
        if value not in ['pending', 'completed']:
            raise serializers.ValidationError("Invalid status. Status must be either 'pending' or 'completed'")
        return value

    def create(self, validated_data):
        # Extract the entity_name data from validated_data
        client = validated_data.pop('client')
        #checking if the entity_name exists in the entity table
        query = Entity.objects.filter(name__iexact= client)
        if query.exists():
            order = Order.objects.create(entity=query.first(), **validated_data)
            return order
        else:
            raise serializers.ValidationError(f"Entity with name '{client}' does not exist")

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status')
        instance.date = validated_data.get('date')
        client = validated_data.pop('client')

        query = Entity.objects.filter(name__iexact=client)
        if query.exists():
            instance.entity = query.first()
            instance.save()
        else:
            raise serializers.ValidationError(f'{client} not found')
        return instance