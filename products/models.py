from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from manufacturers.models import Manufacturer
from datetime import datetime


class Category(MPTTModel):
    title = 'Category'
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated at')
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    def get_all_products_url(self):
        return reverse('all-products-in-category', kwargs={"slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'


def upload_path(instance, filename):
    """
    Generates path to upload images for products (see class Product)
    """
    # Remove all symbols from instance name except alphanumeric
    name = ''.join(x for x in instance.name if x.isalnum())
    if name == '':
        raise ValidationError("Can't save image! Check item name! It's empty after removing all symbols "
                              "except alphanumeric. "
                              "Does it consist from special characters only?")
    return 'images/products/%s/%s' % (name, filename)


class Product(models.Model):
    title = 'Product'
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated at')
    name = models.CharField(max_length=128)
    category = TreeManyToManyField(Category)
    image = models.ImageField(upload_to=upload_path,
                              blank=True,
                              null=True)
    short_description = models.CharField(max_length=64,
                                   blank=True,
                                   null=True, help_text='Maximum 64 symbols')
    description = models.TextField(max_length=1200,
                                  blank=True,
                                  null=True)
    price = MoneyField(max_digits=14,
                       decimal_places=2,
                       default_currency='EUR',
                       blank=True,
                       null=True,
                       verbose_name='Price')

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1)

    # Place of origin, may not be equal to the country of manufacturer
    country = models.CharField(max_length=64, default='')

    publish = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={"pk": self.pk})
