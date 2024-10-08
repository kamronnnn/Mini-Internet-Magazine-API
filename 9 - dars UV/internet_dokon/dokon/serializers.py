from .models import Product, Category, Customer, OrderProduct

from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'
