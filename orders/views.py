from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from cart.models import CartProduct
from .forms import OrderForm


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
        oform = OrderForm(self.request.GET, **kwargs)
        oform.is_valid()
        context['oform'] = oform
        return context


class OrderSubmitView(View):

    def post(self, request, *args, **kwargs):
        address = self.request.POST.get('delivery_address')
        return render(request, 'orders/order_submit.html', {'address': address})
