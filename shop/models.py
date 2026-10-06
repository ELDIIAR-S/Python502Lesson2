from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=[(i, str(i)) for i in range(1, 6)],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв на {self.product.name} ({self.stars}★)'

# from django.db import models
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         related_name="products"
#     )
#
#     def __str__(self):
#         return self.name
#
#
# class Review(models.Model):
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE,
#         related_name="reviews"
#     )
#     text = models.TextField()
#     stars = models.PositiveIntegerField(
#         choices=[
#             (1, "1 звезда"),
#             (2, "2 звезды"),
#             (3, "3 звезды"),
#             (4, "4 звезды"),
#             (5, "5 звезд"),
#         ]
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.product.name} - {self.stars} звезд"