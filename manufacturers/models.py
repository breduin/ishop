from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    title = 'Manufacturer'
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated at')
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=32)
    description = models.TextField(max_length=1200,
                                  blank=True,
                                  null=True)
    web = models.URLField(default='')
    publish = models.BooleanField(default=True)
    country = models.CharField(max_length=64, default='')

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={"pk": self.pk})
