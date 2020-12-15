from django.urls import path, include
from .views import products, get_category

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:pk>', get_category, name='category'),
]