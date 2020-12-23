from django.urls import path
from .views import CartView, AddToCartView, DeleteCartProductView, ChangeQtyView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove-product/<int:pk>/', DeleteCartProductView.as_view(), name='remove-from-cart'),
    path('change-quantity/<int:pk>/', ChangeQtyView.as_view(), name='change-qty'),
]