from django.db import models
from products.models import Product


class CartProduct(models.Model):
    title = 'Cart product'
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated at')

