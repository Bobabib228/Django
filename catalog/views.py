from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView


def contacts(request):
    return render(request, "contacts.html")


def general(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context)
