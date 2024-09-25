from rest_framework import viewsets
from .models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
