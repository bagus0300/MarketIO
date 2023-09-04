from django.contrib import admin
from .models import Product, ProductCategory, ProductImage

class ProductImageInline(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)