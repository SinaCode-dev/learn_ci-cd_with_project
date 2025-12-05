from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import ApplicationSerializer, ServiceSerializer, CommentSerializer, CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer, DiscountSerializer
from .models import Application, Service, Comment, Cart, CartItem, Order, OrderItem, Discount


class ApplicationViewSet(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        application_pk = self.kwargs["application_pk"]
        return Service.objects.filter(application_id=application_pk).all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        application_pk = self.kwargs["application_pk"]
        service_pk = self.kwargs["service_pk"]
        return Comment.objects.filter(service_id=service_pk, service__application_id=application_pk).all()


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    
    def get_queryset(self):
        cart_pk = self.kwargs["cart_pk"]
        return CartItem.objects.filter(cart_id=cart_pk).all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemsViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        order_pk = self.kwargs["order_pk"]
        return OrderItem.objects.filter(order_id=order_pk).all()


class DiscountViewSet(ModelViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class DiscountServicesViewSet(ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        discount_pk = self.kwargs["discount_pk"]
        return Service.objects.filter(discounts_id=discount_pk).all()
    