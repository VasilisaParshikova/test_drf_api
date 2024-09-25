from rest_framework import serializers
from .models import Product, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), source='brand', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'brand', 'brand_id', 'model', 'name', 'description', 'specifications']
