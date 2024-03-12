from django.shortcuts import render
from users.models import *
from products.models import *
import random
from django.contrib.auth.decorators import login_required
import stripe
import os
from dotenv import load_dotenv


load_dotenv()

def home_view(request):
    """
    Renders the home page view.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page template.
    """
    # SELECT ALL FEATURED PRODUCTS
    featured_products = Product.objects.filter(is_featured=True).prefetch_related(
        "productimage_set"
    )
    # CONTROL MAX FEATURED PRODUCTS TO SHOW
    num_featured_to_show = min(len(featured_products), 6)
    featured_products = random.sample(list(featured_products), num_featured_to_show)

    # SELECT ALL SALE PRODUCTS
    sale_products = Product.objects.filter(sale_price__gt=0).prefetch_related(
        "productimage_set"
    )
    # CONTROL MAX SALE PRODUCTS TO SHOW
    num_sale_to_show = min(len(sale_products), 6)
    sale_products = random.sample(list(sale_products), num_sale_to_show)

    context = {
        "featured_products": featured_products,
        "sale_products": sale_products,
    }
    return render(request, "home/home.html", context)
