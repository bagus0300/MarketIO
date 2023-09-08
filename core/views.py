from django.shortcuts import render
from .models import Product, ProductImage
import random
from django.db.models import Prefetch


def home_view(request):
    # SELECT ALL FEATURED PRODUCTS
    featured_products = Product.objects.filter(is_featured=True)
    # CONTROL MAX FEATURED PRODUCTS TO SHOW
    num_featured_to_show = min(len(featured_products), 6)
    featured_products = random.sample(list(featured_products), num_featured_to_show)

    # SELECT ALL SALE PRODUCTS
    sale_products = Product.objects.filter(sale_price__gt=0)
    # CONTROL MAX SALE PRODUCTS TO SHOW
    num_sale_to_show = min(len(sale_products), 6)
    sale_products = random.sample(list(sale_products), num_sale_to_show)

    context = {
        "featured_products": featured_products,
        "sale_products": sale_products,
    }
    return render(request, "home/home.html", context)


def products_view(request):
    products = Product.objects.all().prefetch_related("productimage_set")
    context = {
        "products": products,
    }
    return render(request, "products/products_view.html", context)


def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail_view.html", context)
