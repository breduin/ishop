from django import template
from ..models import CartProduct
from django.db.models import Sum

register = template.Library()

def get_query():
    return CartProduct.objects.all()

@register.inclusion_tag('cart_total_qty.html', takes_context=True)
def cart_total_qty(context):
    """
    Generates total quantity of items in shopping cart.
    :return:
    """
    user = context['user']
    qs = get_query()

    return {'total_qty': qs.aggregate(Sum('qty'))['qty__sum'] }


@register.inclusion_tag('cart_total_cost.html', takes_context=True)
def cart_total_cost(context):
    """
    Generates total cost of items in shopping cart.
    :return:
    """
    user = context['user']
    query = get_query()
    total_cost = 0
    for item in query:
        if item.product.price and item.qty:
            total_cost += item.product.price * item.qty

    return {'total_cost': total_cost }