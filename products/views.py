from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category


def get_catalog(request):
    return render(request, "products/products.html", {'categories': Category.objects.all()})


def get_product(request):
    return render(request, "products.html", {'categories': Category.objects.all()})


def get_category(request):
    return render(request, "products.html", {'categories': Category.objects.all()})


class ProductsByCategoryView(ListView):
    template_name = 'products/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs["pk"], publish=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        category = Category.objects.get(pk=self.kwargs["pk"])
        context['category'] = category
        context['crumbs'] = category.get_ancestors()
        return context
