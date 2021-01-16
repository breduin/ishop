from django.shortcuts import render
from django.views.generic import ListView
from cart.models import CartProduct


class OrderView(ListView):
    template_name = 'orders/order_view.html'
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

