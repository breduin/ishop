from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category
from django.db.models import Q
import structlog

logger = structlog.get_logger(__name__)

def get_catalog(request):
    return render(request, "products/products.html", {'categories': Category.objects.all()})


def get_product(request):
    return render(request, "products.html", {'categories': Category.objects.all()})


def get_category(request):
    return render(request, "products.html", {'categories': Category.objects.all()})


class ProductsByCategoryView(ListView):
    template_name = 'products/products_by_category.html'
    context_object_name = 'products'

    def _get_category(self) -> Category:
        """ Returns the Category object with pk from kwargs """
        return Category.objects.get(pk=self.kwargs["pk"])

    def get_queryset(self):
        """ Returns queryset of Products for given Category and all its descendants"""
        category = self._get_category()
        descendants = category.get_descendants()
        q_ = Q(category__pk=self.kwargs["pk"])
        for descendant in descendants:
            q_ |= Q(category__pk=descendant.pk)
        return Product.objects.filter(q_, publish=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        category = self._get_category()
        context['category'] = category
        context['crumbs'] = category.get_ancestors()

        descendants = category.get_descendants(include_self=True)
        grouped = {}
        for item in descendants:
            qs = Product.objects.filter(category__pk=item.pk)[:3]
            grouped[item.name] = qs

        context['products_by_category'] = grouped
        return context
