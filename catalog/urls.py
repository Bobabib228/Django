from django.contrib import admin
from django.urls import path, include
from django.views import View

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, contacts

app_name = CatalogConfig.name

urlpatterns = [
    #path('', home, name='home'),
    path('contacts/',contacts, name='contacts' ),
    path('', ProductListView.as_view(), name='product_general' ),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail' ),
]
