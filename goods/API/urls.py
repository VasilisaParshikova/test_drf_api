from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, BrandViewSet

router = DefaultRouter()
router.register(r'goods', ProductViewSet, basename='product')
router.register(r'brands', BrandViewSet, basename='drand')

urlpatterns = [
    path('', include(router.urls)),
]
