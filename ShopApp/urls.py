from django.urls import re_path as url
from django.urls import path

from ShopApp import views

urlpatterns=[
    url(r'^apiproducts/$', views.productAPI),
    url(r'^product/([0-9]+)$',views.productAPI),
    path('searchProducts/<str:search>',views.searchProductsAPI)
]