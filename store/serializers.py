from rest_framework import serializers

from .models import Application, Service, Comment, Cart, CartItem, Order, OrderItem, Discount


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["title", "description", "top_service"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["name", "description", "price"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "body", "datetime_created"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "datetime_created"]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "service"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["customer", "datetime_created", "status"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "service", "price"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "name"]