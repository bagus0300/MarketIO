from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductVariant
from users.models import UserFavourite
from .forms import ProductForm, ProductImageForm, ProductVariantForm
from django.urls import reverse
from django.contrib import messages


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


def add_product(request):
    if request.user.is_superuser is False:
        return redirect(reverse("home"))
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()

            # Process variant forms
            for size, _ in ProductVariant.SIZES:
                quantity = request.POST.get(f"quantity_{size}")
                if quantity == "":
                    quantity = 0  # Convert empty strings to None
                ProductVariant.objects.create(
                    product=product, size=size, quantity=quantity
                )
            messages.success(request, "Product added successfully")
            return redirect(
                reverse("add_product")
            )  # Redirect to the same page for a new entry
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()

    variant_choices = ProductVariant.SIZES
    return render(
        request,
        "products/add_product.html",
        {
            "product_form": product_form,
            "image_form": image_form,
            "variant_choices": variant_choices,
        },
    )


def edit_product(request, product_id):
    if request.user.is_superuser is False:
        return redirect(reverse("home"))

    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product = product_form.save()

            # Update or create product image
            if product.productimage_set.exists():
                image = product.productimage_set.first()
                image_form = ProductImageForm(
                    request.POST, request.FILES, instance=image
                )
            else:
                image_form = ProductImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                image = image_form.save(commit=False)
                image.product = product
                image.save()

            # Process variant forms
            for variant in product.variants.all():
                variant.product = product
                quantity = request.POST.get(f"quantity_{variant.size}")
                variant.quantity = quantity
                variant.save()
            messages.success(request, "Product edited successfully")
            return redirect(
                reverse("edit_product", args=[product.id])
            )  # Redirect to the same page after editing
    else:
        product_form = ProductForm(instance=product)
        image = product.productimage_set.first()
        if image:
            image_form = ProductImageForm(instance=image)
        else:
            image_form = ProductImageForm()

    variant_choices = ProductVariant.SIZES
    variants_data = [
        {"size": variant.size, "quantity": variant.quantity}
        for variant in product.variants.all()
    ]
    variant_formset = [ProductVariantForm(data) for data in variants_data]

    return render(
        request,
        "products/edit_product.html",
        {
            "product": product,
            "product_form": product_form,
            "image_form": image_form,
            "variant_choices": variant_choices,
            "variant_formset": variant_formset,
            "variants_data": variants_data,
        },
    )


def delete_product(request, product_id):
    if request.user.is_superuser is False:
        return redirect(reverse("home"))

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully")
    return redirect(reverse("products"))
