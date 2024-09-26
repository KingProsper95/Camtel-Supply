from rest_framework import serializers
from CamtelSupplyAPI.models import Category, Product
from CamtelSupplyAPI.serializers.categorySerializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'category', 'created_at']
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_name = category_data.get('name')

        # Try to get the category if it exists, otherwise create a new one
        category, created = Category.objects.get_or_create(
            name__iexact=category_name,
            defaults=category_data
        )

        # Now create the product with the existing or new category
        product = Product.objects.create(category=category, **validated_data)

        return product
    
    def update(self, instance, validated_data):
        category_name = validated_data.pop('category').get('name')
        instance.name = validated_data.get('name')

        #check if the category with the given name is present in the database
        query = Category.objects.filter(name__iexact=category_name)
        if query.exists():
            instance.category = query.first()
            instance.save()
        else:
            raise serializers.ValidationError(
            {"detail" : f"'{category_name}' not found"}
            )
        return instance
