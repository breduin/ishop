from django.shortcuts import render
from django.views.generic import ListView, DetailView


class ManufacturersListView(DetailView):
    template_name = 'manufacturers_list.html'


class ManufacturerDetailView(DetailView):
    template_name = 'manufacturers_detail.html'
