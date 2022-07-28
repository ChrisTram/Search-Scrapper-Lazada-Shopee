from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import random
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
        return defaultProducts(search)
    #   return JsonResponse("API not implemented")
    
    

def defaultProducts(choice):
    choices=['smartphone' , 'smartphones' ,'perfume' ,'perfumes' , 'clothe' , 'clothes']
    if(choice not in choices): choice = random.choice(["smartphone","perfume","clothes"])
    if(choice == "smartphone" or choice == 'smartphones') :
        objects = [{'ProductName':"LG Optimus", 'ProductBrand':"LG", 'ProductWeb':"Shopee"},
                   {'ProductName':"LG G Pro 2", 'ProductBrand':"LG", 'ProductWeb':"Lazada"},
                   {'ProductName':"LG G Flex 1", 'ProductBrand':"LG", 'ProductWeb':"Lazada"},
                   {'ProductName':"Honor X30", 'ProductBrand':"Honor", 'ProductWeb':"Shopee"},
                   {'ProductName':"Honor X20", 'ProductBrand':"Honor", 'ProductWeb':"Lazada"},
                   {'ProductName':"Honor 20 View", 'ProductBrand':"Honor", 'ProductWeb':"Shopee"},
                   {'ProductName':"Iphone X", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
                   {'ProductName':"Sony Xperia Z", 'ProductBrand':"Sony", 'ProductWeb':"Lazada"},
                   {'ProductName':"Sony Xperia Play", 'ProductBrand':"Sony", 'ProductWeb':"Lazada"},
                   {'ProductName':"Sony Xperia Z", 'ProductBrand':"Sony", 'ProductWeb':"Shopee"},
                   {'ProductName':"Sony Xperia Z", 'ProductBrand':"Sony", 'ProductWeb':"Lazada"},
                   {'ProductName':"Iphone X Pro", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
                   {'ProductName':"Nokia Lumia 6", 'ProductBrand':"Nokia", 'ProductWeb':"Lazada"},
                   {'ProductName':"Nokia Eclipse", 'ProductBrand':"Nokia", 'ProductWeb':"Lazada"},
                   {'ProductName':"Iphone X Pro", 'ProductBrand':"Apple", 'ProductWeb':"Lazada"},
                   {'ProductName':"Iphone X Pro", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
                   {'ProductName':"Iphone 9", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
                   {'ProductName':"Samsung S21", 'ProductBrand':"Samsung", 'ProductWeb':"Lazada"},
                   {'ProductName':"Samsung S22", 'ProductBrand':"Samsung", 'ProductWeb':"Lazada"},
                   {'ProductName':"Samsung S21", 'ProductBrand':"Samsung", 'ProductWeb':"Shopee"},
                   {'ProductName':"Samsung S20", 'ProductBrand':"Samsung", 'ProductWeb':"Lazada"},
                   {'ProductName':"Samsung S20", 'ProductBrand':"Samsung", 'ProductWeb':"Lazada"},
                   {'ProductName':"Iphone X Pro", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
                   {'ProductName':"Huawei P30", 'ProductBrand':"Huawei", 'ProductWeb':"Shopee"},
                   {'ProductName':"Huawei P20", 'ProductBrand':"Huawei", 'ProductWeb':"Lazada"},
                   {'ProductName':"Huawei Nova 9", 'ProductBrand':"Huawei", 'ProductWeb':"Shopee"},
                   {'ProductName':"Huawei P30", 'ProductBrand':"Huawei", 'ProductWeb':"Lazada"},
                   {'ProductName':"Iphone X", 'ProductBrand':"Apple", 'ProductWeb':"Lazada"}]
    elif(choice == "perfume" or choice == "perfumes") :
        objects = [{'ProductName':"Chanel 5", 'ProductBrand':"Chanel", 'ProductWeb':"Shopee"},
                   {'ProductName':"Chanel 5", 'ProductBrand':"Chanel", 'ProductWeb':"Lazada"},
                   {'ProductName':"Bleu de Chanel", 'ProductBrand':"Chanel", 'ProductWeb':"Lazada"},
                   {'ProductName':"Shalimar", 'ProductBrand':"Guerlain", 'ProductWeb':"Shopee"},
                   {'ProductName':"Shalimar", 'ProductBrand':"Guerlain", 'ProductWeb':"Lazada"},
                   {'ProductName':"Mon Guerlain", 'ProductBrand':"Guerlain", 'ProductWeb':"Shopee"},
                   {'ProductName':"Mon Guerlain", 'ProductBrand':"Guerlain", 'ProductWeb':"Lazada"},
                   {'ProductName':"La Petite Robe Noire", 'ProductBrand':"Guerlain", 'ProductWeb':"Lazada"},
                   {'ProductName':"Bombshell", 'ProductBrand':"Victoria's Secret", 'ProductWeb':"Shopee"},
                   {'ProductName':"Bare Vanilla", 'ProductBrand':"Victoria's Secret", 'ProductWeb':"Shopee"},
                   {'ProductName':"Pure Seduction", 'ProductBrand':"Victoria's Secret", 'ProductWeb':"Lazada"},
                   {'ProductName':"Bombshell", 'ProductBrand':"Victoria's Secret", 'ProductWeb':"Lazada"},
                   {'ProductName':"Bare Vanilla", 'ProductBrand':"Victoria's Secret", 'ProductWeb':"Lazada"},
                   {'ProductName':"Pure Seduction", 'ProductBrand':"Victoria's Secret", 'ProductWeb':"Shopee"},
                   {'ProductName':"J'adore", 'ProductBrand':"Dior", 'ProductWeb':"Lazada"},
                   {'ProductName':"Idôle", 'ProductBrand':"Lancôme", 'ProductWeb':"Shopee"},
                   {'ProductName':"Tresor", 'ProductBrand':"Lancôme", 'ProductWeb':"Lazada"},
                   {'ProductName':"Tresor", 'ProductBrand':"Lancôme", 'ProductWeb':"Shopee"},
                   {'ProductName':"Iphone 9", 'ProductBrand':"Apple", 'ProductWeb':"Shopee"},
                   {'ProductName':"Acqua Di Gio", 'ProductBrand':"Armani", 'ProductWeb':"Lazada"},
                   {'ProductName':"Acqua Di Gio Absolu", 'ProductBrand':"Armani", 'ProductWeb':"Lazada"},
                   {'ProductName':"Acqua Di Gio", 'ProductBrand':"Armani", 'ProductWeb':"Shopee"},
                   {'ProductName':"Black Code", 'ProductBrand':"Armani", 'ProductWeb':"Lazada"},
                   {'ProductName':"Fahrenheit", 'ProductBrand':"Christian Dior", 'ProductWeb':"Lazada"},
                   {'ProductName':"HUGO BOSS", 'ProductBrand':"HUGO BOSS", 'ProductWeb':"Shopee"},
                   {'ProductName':"HUGO Energise", 'ProductBrand':"HUGO BOSS", 'ProductWeb':"Shopee"},
                   {'ProductName':"HUGO BOSS", 'ProductBrand':"HUGO BOSS", 'ProductWeb':"Lazada"},
                   {'ProductName':"Lacoste pour Homme", 'ProductBrand':"Lacoste", 'ProductWeb':"Shopee"},
                   {'ProductName':"Lacoste pour Homme", 'ProductBrand':"Lacoste", 'ProductWeb':"Lazada"},
                   {'ProductName':"Gucci Rush", 'ProductBrand':"GUCCI", 'ProductWeb':"Lazada"}]  
    elif(choice == "clothe" or choice == "clothes") :
        objects = [{'ProductName':"T-Shirt", 'ProductBrand':"Zara", 'ProductWeb':"Shopee"},
                   {'ProductName':"Polo", 'ProductBrand':"Zara", 'ProductWeb':"Lazada"},
                   {'ProductName':"Jean", 'ProductBrand':"LEVIS", 'ProductWeb':"Lazada"},
                   {'ProductName':"Jean", 'ProductBrand':"LEVIS", 'ProductWeb':"Shopee"},
                   {'ProductName':"Hoodie", 'ProductBrand':"Adidas", 'ProductWeb':"Shopee"},
                   {'ProductName':"Shoes", 'ProductBrand':"Adidas", 'ProductWeb':"Lazada"},
                   {'ProductName':"Socks", 'ProductBrand':"Adidas", 'ProductWeb':"Shopee"},
                   {'ProductName':"Cap", 'ProductBrand':"Adidas", 'ProductWeb':"Lazada"},
                   {'ProductName':"La Petite Robe Noire", 'ProductBrand':"Adidas", 'ProductWeb':"Lazada"},
                   {'ProductName':"Bag", 'ProductBrand':"Louis Vuitton", 'ProductWeb':"Shopee"},
                   {'ProductName':"Shoes", 'ProductBrand':"Louis Vuitton", 'ProductWeb':"Shopee"},
                   {'ProductName':"Bag", 'ProductBrand':"Louis Vuitton", 'ProductWeb':"Lazada"},
                   {'ProductName':"Polo", 'ProductBrand':"Louis Vuitton", 'ProductWeb':"Lazada"},
                   {'ProductName':"Dress", 'ProductBrand':"Louis Vuitton", 'ProductWeb':"Lazada"},
                   {'ProductName':"Dress", 'ProductBrand':"Louis Vuitton", 'ProductWeb':"Shopee"},
                   {'ProductName':"Shoes", 'ProductBrand':"Nike", 'ProductWeb':"Lazada"},
                   {'ProductName':"Sport T Shirt", 'ProductBrand':"Nike", 'ProductWeb':"Shopee"},
                   {'ProductName':"Short", 'ProductBrand':"Nike", 'ProductWeb':"Lazada"},
                   {'ProductName':"Cap", 'ProductBrand':"Nike", 'ProductWeb':"Shopee"},
                   {'ProductName':"Polo", 'ProductBrand':"Hermès", 'ProductWeb':"Shopee"},
                   {'ProductName':"Dress", 'ProductBrand':"Hermès", 'ProductWeb':"Lazada"},
                   {'ProductName':"Polo", 'ProductBrand':"Hermès", 'ProductWeb':"Lazada"},
                   {'ProductName':"Polo", 'ProductBrand':"H&M", 'ProductWeb':"Lazada"},
                   {'ProductName':"Skirt", 'ProductBrand':"H&M", 'ProductWeb':"Lazada"},
                   {'ProductName':"Gloves", 'ProductBrand':"H&M", 'ProductWeb':"Shopee"},
                   {'ProductName':"Tie", 'ProductBrand':"H&M", 'ProductWeb':"Lazada"},
                   {'ProductName':"Manga Theme T Shirt", 'ProductBrand':"Uniqlo", 'ProductWeb':"Lazada"},
                   {'ProductName':"Polo", 'ProductBrand':"Uniqlo", 'ProductWeb':"Shopee"},
                   {'ProductName':"Wallet", 'ProductBrand':"Prada", 'ProductWeb':"Shopee"},
                   {'ProductName':"Dress", 'ProductBrand':"Prada", 'ProductWeb':"Lazada"},
                   {'ProductName':"Wallet", 'ProductBrand':"Prada", 'ProductWeb':"Lazada"},
                   {'ProductName':"Dress", 'ProductBrand':"Prada", 'ProductWeb':"Shopee"},
                   {'ProductName':"Polo", 'ProductBrand':"Lacoste", 'ProductWeb':"Shopee"},
                   {'ProductName':"Cap", 'ProductBrand':"Lacoste", 'ProductWeb':"Lazada"},
                   {'ProductName':"Bag", 'ProductBrand':"Lacoste", 'ProductWeb':"Lazada"},          
                   {'ProductName':"Wallet", 'ProductBrand':"Lacoste", 'ProductWeb':"Lazada"}] 
    Products.objects.all().delete()
    products_serializer=ProductSerializer(data=objects, many=True)
    if products_serializer.is_valid():
        products_serializer.save()
        return JsonResponse(products_serializer.data, safe=False)
    return JsonResponse("Failed.", safe=False)


