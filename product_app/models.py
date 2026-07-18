from django.db import models
from django.utils.text import slugify


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=10)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.is_available = self.stock > 0
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    BADGE_CHOICES = [
        ("new", "New"),
        ("discounted", "Discounted"),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    badge = models.CharField(max_length=100, choices=BADGE_CHOICES, default="new")

    def __str__(self):
        return f"{self.product.name}'s description"