from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from ShopApp.models import Products
from ShopApp.serializers import ProductSerializer
# Create your views here.

from scraper_api import ScraperAPIClient

def productAPI(request, id=0):
    if request.method=='GET':
        products = Products.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer = ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Added Successfully.", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product=Products.objects.get(ProductID=product_data['ProductID'])
        products_serializer=ProductSerializer(product, data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Update successfully", safe=False)
    elif request.method=='DELETE':
        product=Products.objects.get(ProductID=id)
        #if product is None:
        product.delete()
        return JsonResponse("Deleted successfully")


from django.shortcuts import render

def searchProductsAPI(request, search =""):
    if request.method=='GET':
        return searchProducts(search)
        # products = Products.objects.all()
        # products_serializer = ProductSerializer(products, many=True)
        # return JsonResponse(products_serializer.data, safe=False)


def searchProducts(search):
    Products.objects.all().delete()
    objects = [{'ProductName':"LG99999999999", 'ProductBrand':"LG", 'ProductWeb':"Shopee"},
               {'ProductName':"Sony999999", 'ProductBrand':"Sony", 'ProductWeb':"Lazada"},
               {'ProductName':"Sony999999", 'ProductBrand':"Chanel", 'ProductWeb':"Lazada"},
               {'ProductName':"Sony999999", 'ProductBrand':"Chanel", 'ProductWeb':"Shopee"},
               {'ProductName':"Sony999999", 'ProductBrand':"Sony", 'ProductWeb':"Lazada"},
               {'ProductName':"Sony999999", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
               {'ProductName':"Sony999999", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
               {'ProductName':"Sony999999", 'ProductBrand':"Apple", 'ProductWeb':"Lazada"}]
    products_serializer=ProductSerializer(data=objects, many=True)
    if products_serializer.is_valid():
        products_serializer.save()
        return JsonResponse(products_serializer.data, safe=False)
    return JsonResponse("Failed.", safe=False)
