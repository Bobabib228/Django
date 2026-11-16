from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    return render(request, "catalog/contacts.html")
