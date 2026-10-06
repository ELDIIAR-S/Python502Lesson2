from django.urls import path

from .views import CategoryListView, ProductReviewsListView

urlpatterns = [
    path('products/reviews/', ProductReviewsListView.as_view()),
    path('categories/', CategoryListView.as_view()),
]