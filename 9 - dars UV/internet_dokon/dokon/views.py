from .models import Product, Category, Customer, OrderProduct
from .serializers import ProductSerializer, CategorySerializer, CustomerSerializer, OrderProductSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderProductViewSet(ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

