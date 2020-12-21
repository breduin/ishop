from django.urls import path
from .views import CartView, AddToCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
]