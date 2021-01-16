from django.db import models
from products.models import Product


class CartProduct(models.Model):
    title = 'Cart product'
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated at')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    @property
    def sum(self):
        if self.product.price:
            return self.product.price*self.qty
        else:
            return 0

