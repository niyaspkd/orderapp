from rest_framework import serializers
from .models import Products, Customer, Order, Cart


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

     class Meta:
        model = Customer
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'
