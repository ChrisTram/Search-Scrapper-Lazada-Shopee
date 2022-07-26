from django.urls import re_path as url
from ShopApp import views

urlpatterns=[
    url(r'^products/$', views.productAPI),
    url(r'^product/([0-9]+)$',views.productAPI),
]