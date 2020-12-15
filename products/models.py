from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"pk": self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = 'Product'
    name = models.CharField(max_length=128)
    category = TreeManyToManyField(Category)

    def __str__(self):
        return '%s' % self.name
