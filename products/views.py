from django.shortcuts import render
from .models import Category

# Create your views here.

def products(request):
    return render(request, "products.html", {'categories': Category.objects.all()})

def get_category(request):
    return render(request, "products.html", {'categories': Category.objects.all()})