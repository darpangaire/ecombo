from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)
    # size = models.ForeignKey(Size,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)  # e.g., S, M, L, XL
    # color=models.Fore(Color,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"



