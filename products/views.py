from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
        """ Returns the Category object with slug from kwargs """

        return Category.objects.get(slug=self.kwargs["slug"])

    def get_queryset(self):
        """ Returns queryset of Products for given Category and all its descendants"""
        category = self._get_category()
        descendants = category.get_descendants()
        q_ = Q(category__slug=self.kwargs["slug"])
        for descendant in descendants:
            q_ |= Q(category__slug=descendant.slug)

        return Product.objects.filter(q_, publish=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        category = self._get_category()
        context['category'] = category
        context['crumbs'] = category.get_ancestors()

        # Generates the output of products by categories,
        # since 'regroup' tag in template does not work for M2M field
        descendants = category.get_descendants(include_self=True)
        grouped = {}
        for item in descendants:
            qs = Product.objects.filter(category__pk=item.pk)[:3]
            grouped[item.name] = (item, qs, )
        context['products_by_category'] = grouped

        return context


class AllProductsInCategoryView(ListView):
    template_name = 'products/all_products_in_category.html'
    context_object_name = 'products'

    def _get_category(self) -> Category:
        """ Returns the Category object with slug from kwargs """
        return Category.objects.get(slug=self.kwargs["slug"])

    def get_queryset(self):
        """ Returns queryset of Products for given Category and all its descendants"""
        category = self._get_category()
        descendants = category.get_descendants()
        q_ = Q(category__slug=self.kwargs["slug"])
        for descendant in descendants:
            q_ |= Q(category__slug=descendant.slug)
        return Product.objects.filter(q_, publish=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        category = self._get_category()
        context['category'] = category
        context['crumbs'] = category.get_ancestors()

        return context


class ProductDetailView(DetailView):
    template_name = 'products/product_detail_view.html'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        this_categories = Product.objects.get(pk=self.kwargs["pk"]).category
        breadcrumbs = list()
        for category in this_categories.all():
            breadcrumbs.append(category.get_ancestors(include_self=True))
        context['breadcrumbs'] = breadcrumbs

        return context
