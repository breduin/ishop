from django.db import models
from cart.models import CartProduct

class Order(models.Model):
    title = 'Order'
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated at')
    status_list = [
        ('active', 'active'),
        ('payed', 'payed'),
        ('done', 'done'),
    ]
    status = models.CharField(max_length=16, choices=status_list, default='active')

    def __str__(self):
        return "Order #%d" % self.pk

    @property
    def total_cost(self):
        total = 0
        for item in self.product.all():
            total += item.sum