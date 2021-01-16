from django.urls import path
from .views import get_product, get_catalog, ProductsByCategoryView, AllProductsInCategoryView, ProductDetailView

urlpatterns = [
    path('', get_catalog, name='catalog'),
    path('category/<str:slug>/all/', AllProductsInCategoryView.as_view(), name='all-products-in-category'),
    path('category/<str:slug>/', ProductsByCategoryView.as_view(), name='category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]