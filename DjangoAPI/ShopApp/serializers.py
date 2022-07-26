from rest_framework import serializers
from ShopApp.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('ProductID',
                  'ProductName',
                  'ProductBrand',
                  'ProductWeb')
