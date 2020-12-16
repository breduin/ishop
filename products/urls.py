from django.urls import path
from .views import get_product, get_catalog, ProductsByCategoryView

urlpatterns = [
    path('', get_catalog, name='catalog'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='category'),
    path('product/<int:pk>/', get_product, name='product'),
]