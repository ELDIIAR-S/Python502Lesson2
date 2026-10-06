from django.db.models import Count
from rest_framework.generics import ListAPIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductReviewsSerializer


class ProductReviewsListView(ListAPIView):
    queryset = Product.objects.prefetch_related('reviews')
    serializer_class = ProductReviewsSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.annotate(products_count=Count('products'))
    serializer_class = CategorySerializer