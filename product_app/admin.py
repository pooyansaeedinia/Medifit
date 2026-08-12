from django.contrib import admin

from .models import Brand, Category, Comments, Product, ProductBadge, ProductDescription

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Brand)
admin.site.register(ProductBadge)
admin.site.register(ProductDescription)
