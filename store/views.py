from rest_framework import generics
from .models.category import Category
from .models.product import Product
from .models.order import Order, OrderItem
from .models.cart import Cart, CartItem
from .models.shipping import ShippingAddress
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer,
    CartSerializer,
    CartItemSerializer,
    ShippingAddressSerializer,
)

# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Order Views
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# OrderItem Views
class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# Cart Views
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# CartItem Views
class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

# ShippingAddress Views
class ShippingAddressListCreateView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

class ShippingAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
