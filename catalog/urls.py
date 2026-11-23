from django.contrib import admin
from django.urls import path, include
from django.views import View

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, contacts, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    #path('', home, name='home'),
    path('contacts/',contacts, name='contacts' ),
    path('', ProductListView.as_view(), name='product_general' ),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail' ),
    path('product/create/', ProductCreateView.as_view(), name='product_create' ),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update' ),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
