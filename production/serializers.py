from rest_framework import serializers
from .models import Product, ProductMaterial, WarehouseQuantity


class WarehouseQuantitySerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source='raw_material.name')

    class Meta:
        model = WarehouseQuantity
        fields = ('material_name', 'remainder', 'price')


class ProductMaterialSerializer(serializers.ModelSerializer):
    raw_material = WarehouseQuantitySerializer(many=True, read_only=True)

    class Meta:
        model = ProductMaterial
        fields = ('raw_material',)


class ProductSerializer(serializers.ModelSerializer):
    product_materials = ProductMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'product_materials')
