from rest_framework import serializers
from .models import Category, Product, Variant, Option

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category_id', 'name', 'price', 'card_color', 'image')

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('id', 'name', 'product_id')

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'name', 'card_color', 'price', 'step', 'image', 'product_id')


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')