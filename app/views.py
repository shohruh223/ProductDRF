from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from app.models import Category, Product
from app.serializers import CategoryModelSerializer, ProductModelSerializer


class CategoryView(ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


class ProductView(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'created_at', 'price']
    search_fields = ['title', 'price']
