from rest_framework import serializers
from product.models import Product, Category, Review




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title description price image'.split()



class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category 
        fields ='name'.split()


class CategoryDetailSerializer( serializers.ModelSerializer):
    class Meta:
        model=Category
        fields ='__all__'





class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='text product'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields ='__all__'