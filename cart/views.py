from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View
from products.models import Product
from .models import CartProduct


class CartView(ListView):
    template_name = 'cart/cart_view.html'
    context_object_name = 'products'

    def get_queryset(self):
        return CartProduct.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        total_cost = 0
        total_qty = 0
        for product in products:
            if product.product.price and product.qty:
                total_cost += product.qty * product.product.price
                total_qty += product.qty
        context['total_cost'] = total_cost
        context['total_qty'] = total_qty
        return context


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        pk_new = kwargs["pk"]
        product = Product.objects.get(pk=pk_new)
        try:
            newcartproduct = CartProduct.objects.get(product__pk=pk_new)
        except CartProduct.DoesNotExist:
            product.cartproduct_set.create()
        else:
            newcartproduct.qty += 1
            newcartproduct.save(update_fields=['qty'])
        return render(request, 'cart/add_to_cart_view.html')


class DeleteCartProductView(DeleteView):
    model = CartProduct
    success_url = reverse_lazy('cart')


class ChangeQtyView(View):

    def post(self, request, *args, **kwargs):
        p = CartProduct.objects.get(pk=kwargs["pk"])
        p.qty = int(self.request.POST.get('qty'))
        p.save()
        return HttpResponseRedirect(reverse_lazy('cart'))



