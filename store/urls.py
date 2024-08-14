from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    ProductListCreateView,
    ProductDetailView,
    OrderListCreateView,
    OrderDetailView,
    OrderItemListCreateView,
    OrderItemDetailView,
    CartListCreateView,
    CartDetailView,
    CartItemListCreateView,
    CartItemDetailView,
    ShippingAddressListCreateView,
    ShippingAddressDetailView,
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<uuid:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Product URLs
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Order URLs
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<uuid:pk>/', OrderDetailView.as_view(), name='order-detail'),

    # OrderItem URLs
    path('order-items/', OrderItemListCreateView.as_view(), name='order-item-list-create'),
    path('order-items/<uuid:pk>/', OrderItemDetailView.as_view(), name='order-item-detail'),

    # Cart URLs
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<uuid:pk>/', CartDetailView.as_view(), name='cart-detail'),

    # CartItem URLs
    path('cart-items/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('cart-items/<uuid:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),

    # ShippingAddress URLs
    path('shipping-addresses/', ShippingAddressListCreateView.as_view(), name='shipping-address-list-create'),
    path('shipping-addresses/<uuid:pk>/', ShippingAddressDetailView.as_view(), name='shipping-address-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)