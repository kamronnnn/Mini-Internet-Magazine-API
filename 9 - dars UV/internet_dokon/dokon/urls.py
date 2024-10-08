from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CategoryViewSet, CustomerViewSet, OrderProductViewSet

router = SimpleRouter()

router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
