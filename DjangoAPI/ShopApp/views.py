from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ShopApp.models import Products
from ShopApp.serializers import ProductSerializer
# Create your views here.

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
        product=Products.objects.get(ProductId=product_data['ProductID'])
        products_serializer=ProductSerializer(product, data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Update successfully", safe=False)
    elif request.method=='DELETE':
        product=Products.objects.get(ProductID=id)
        #if product is None:
        product.delete()
        return JsonResponse("Deleted successfully")

