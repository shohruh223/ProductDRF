from rest_framework.serializers import ModelSerializer
from app.models import Category, Product


class CategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Category
        exclude = ()


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()