from django.contrib import admin
from django.urls import path
from .views import products, basket_add, basket_remove, product_detail

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('product/<int:id>/<slug:slug>/', product_detail, name='product_detail'),  #
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
