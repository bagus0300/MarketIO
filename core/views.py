from django.shortcuts import render
from .models import *
from users.models import User
import random
from django.db.models import Prefetch
from users.models import UserFavourite
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import stripe
import json
import os
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv('STRIPE_PRIVATE_KEY')



def home_view(request):
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


def products_view(request):
    products = Product.objects.all().prefetch_related("productimage_set")
    context = {
        "products": products,
    }
    return render(request, "products/products_view.html", context)


def product_detail_view(request, product_id):
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


@login_required
def add_remove_user_favourite(request, product_id):
    product = Product.objects.get(id=product_id)
    product_favourite = UserFavourite.objects.filter(user=request.user, product=product)
    if len(product_favourite) > 0:
        product_favourite[0].delete()
        is_favourite = False

    else:
        UserFavourite.objects.create(user=request.user, product_id=product_id)
        is_favourite = True

    context = {
        "is_favourite": is_favourite,
        "product": product,
    }
    return render(request, "products/partials/_favourite_button.html", context)


def add_to_cart(request):
    product = ProductVariant.objects.filter(
        id=request.POST.get("product_variant")
    ).first()
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
    else:
        cart = Cart.objects.get_or_create(session=request.session.session_key)[0]
    quantity = int(request.POST.get("quantity"))
    cart.add_item(product, quantity)
    cart_total_quantity = cart.get_total_items()
    badge_quantity = cart_total_quantity
    if badge_quantity > 99:
        badge_quantity = '99+'
    return HttpResponse(
        (
            "<div id='cart-counter-badge' "
            "hx-swap-oob='true' "
            "class='w-5 h-5 text-center text-white "
            "flex items-center justify-center rounded-full "
            "bg-primary text-[10px] absolute -right-3 "
            f"font-bold -top-1 bg-red-700'>{badge_quantity}</div>"
        )
    )


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart = cart_item.cart
    cart_item.delete()
    cart_total_quantity = cart.get_total_items()
    badge_quantity = cart_total_quantity
    if badge_quantity > 99:
        badge_quantity = '99+'

    return HttpResponse(
        (
            f'<span hx-swap-oob="true" id="subtotal">'
            f"Subtotal: €{cart.get_total_price()}</span>"
            "<div id='cart-counter-badge' "
            "hx-swap-oob='true' "
            "class='w-5 h-5 text-center text-white "
            "flex items-center justify-center rounded-full "
            "bg-primary text-[10px] absolute -right-3 "
            f"font-bold -top-1 bg-red-700'>{badge_quantity}</div>"
        )
    )


def update_cart_quantity(request, cart_item_id, quantity):
    cart_item = CartItem.objects.get(id=cart_item_id)
    print(cart_item)
    cart = cart_item.cart
    print(cart)
    cart_item.quantity = quantity
    print(quantity)
    cart_item.save()
    cart.save()
    print(cart.get_total_price())
    cart_total_quantity = cart.get_total_items()
    badge_quantity = cart_total_quantity
    if badge_quantity > 99:
        badge_quantity = '99+'

    return HttpResponse(
        (
            f'<span hx-swap-oob="true" id="subtotal">'
            f"Subtotal: €{cart.get_total_price()}</span>"
            "<div id='cart-counter-badge' "
            "hx-swap-oob='true' "
            "class='w-5 h-5 text-center text-white "
            "flex items-center justify-center rounded-full "
            "bg-primary text-[10px] absolute -right-3 "
            f"font-bold -top-1 bg-red-700'>{badge_quantity}</div>)"
        )
    )


def cart_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
    else:
        cart = Cart.objects.get_or_create(session=request.session.session_key)[0]
    cart_items = cart.cartitem_set.all()

    context = {
        "cart_items": cart_items,
        "cart": cart,
    }
    return render(request, "cart/cart.html", context)


@login_required
def account_view(request):
    return render(request, 'account/overview.html')

@login_required
def account_orders_view(request):
    return render(request, 'account/orders.html')

@login_required
def account_addresses_view(request):
    return render(request, 'account/addresses.html')

@login_required
def account_favourites_view(request):
    favourite_products = UserFavourite.objects.filter(user=request.user)
    return render(request, 'account/favourites.html', {"favourite_products":favourite_products})

def checkout_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
    else:
        cart = Cart.objects.get_or_create(session=request.session.session_key)[0]
    cart_items = cart.cartitem_set.all()

    context = {
        "cart_items": cart_items,
        "cart": cart,
    }

    return render(request, 'checkout/checkout.html', context)

def create_payment(request):
    try:
        data = json.loads(request.body)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=100,
            currency='usd',
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)