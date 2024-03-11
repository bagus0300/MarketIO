from django.shortcuts import render
from .models import Product
from users.models import UserFavourite


def products_view(request):
    """
    View function for displaying all products.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    products = Product.objects.all().prefetch_related("productimage_set")
    context = {
        "products": products,
    }
    return render(request, "products/products_view.html", context)


def product_detail_view(request, product_id):
    """
    View function to display the details of a product.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    product = Product.objects.get(id=product_id)
    if request.user.is_anonymous:
        is_favourite = False
    else:
        user_favourites = UserFavourite.objects.filter(
            user=request.user, product_id=product_id
        )

        if len(user_favourites) > 0:
            is_favourite = True
        else:
            is_favourite = False

    context = {
        "product": product,
        "is_favourite": is_favourite,
    }
    return render(request, "products/product_detail_view.html", context)