from rest_framework import serializers
from CamtelSupplyAPI.models import Order, Product, OrderDetails
from CamtelSupplyAPI.serializers.productSerializer import ProductSerializer
from CamtelSupplyAPI.serializers.orderSerializer import OrderSerializer
from rest_framework.response import Response

class OrderPublicSerializer(serializers.ModelSerializer):
    entity_name = serializers.CharField(source= 'entity.name', read_only=True)
    client = serializers.CharField(write_only=True)
    class Meta:
        model = Order
        fields = ['id','entity_name', 'date', 'status', 'client']

class OrderDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_name_input = serializers.CharField(write_only=True)
    order = OrderPublicSerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name='orderDetails-detail',
        lookup_field='pk'
    )
    class Meta:
        model = OrderDetails
        fields = ['url', 'id', 'product_name' ,'product_name_input', 'order', 'quantity', 'created_at']

    def validate_product_name_input(self, value):
        '''
        Check if the product exists based on the productName.
        If the product exists, return it; otherwise, raise an error.
        '''
        query = Product.objects.filter(name__iexact=value)
        if query.exists():
            product = query.first()
        else:
            raise serializers.ValidationError(f"Product with name '{value}' does not exist.")
        return product

    def create(self, validated_data):
        #this line removes the name, validates it and returns the instance if valid
        product = validated_data.pop('product_name_input')

        order_data = validated_data.pop('order')

        # Handle order data
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order = order_serializer.save()  # Create or update the order
            details = OrderDetails.objects.create(product=product, order=order, **validated_data)
            return details

        raise serializers.ValidationError(order_serializer.errors)

    def update(self, instance, validated_data):
        # Update the order data if provided
        order_data = validated_data.pop('order')
        if order_data:
            # Update the related order instance using the OrderSerializer
            order_serializer = OrderSerializer(instance=instance.order, data=order_data, partial=True)
            if order_serializer.is_valid():
                order_serializer.save()  # Call the update method of OrderSerializer
            else:
                raise serializers.ValidationError(order_serializer.errors)

        # Update the product
        instance.product = validated_data.pop('product_name_input')

        # Update other fields
        instance.quantity = validated_data.get('quantity', instance.quantity)

        instance.save()

        return instance
