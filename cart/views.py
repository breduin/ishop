from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View
from products.models import Product
from .models import CartProduct
from django.http import HttpResponse


class CartView(ListView):
    template_name = 'cart/cart_view.html'
    context_object_name = 'products'

    def get_queryset(self):
        return CartProduct.objects.all()


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        pk_new = kwargs["pk"]
        product = Product.objects.get(pk=pk_new)
        try:
            newcartproduct = CartProduct.objects.get(product__pk=pk_new)
        except CartProduct.DoesNotExist:
            product.cartproduct_set.create()
        else:
            print('Already in cart!')
        return render(request, 'cart/add_to_cart_view.html')


