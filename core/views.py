# TODO:
# 1 Handle user address selection in checkout
# 2 Add new address form and functionality in checkout
# 3 require login for checkout
# 4 remove country dropdown stripe elements

from django.shortcuts import render
from .models import *
from users.models import *
import random
from django.db.models import Prefetch

# from users.models import UserFavourite
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import stripe
import json
import os
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
import math

load_dotenv()

stripe.api_key = os.getenv("STRIPE_PRIVATE_KEY")


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
        badge_quantity = "99+"
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
        badge_quantity = "99+"

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
        badge_quantity = "99+"

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
    return render(request, "account/overview.html")


@login_required
def account_orders_view(request):
    orders = Order.objects.filter(user=request.user).order_by("-date_created")
    context = {
        "orders": orders,
    }
    return render(request, "account/orders.html", context)


@login_required
def account_addresses_view(request):
    return render(request, "account/addresses.html")


@login_required
def account_favourites_view(request):
    favourite_products = UserFavourite.objects.filter(user=request.user)
    return render(
        request, "account/favourites.html", {"favourite_products": favourite_products}
    )


@login_required
def checkout_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
    else:
        cart = Cart.objects.get_or_create(session=request.session.session_key)[0]
    cart_items = cart.cartitem_set.all()

    context = {
        "cart_items": cart_items,
        "cart": cart,
        "addresses": UserAddress.objects.filter(user=request.user).order_by("id"),
        "default_address": UserAddress.objects.filter(
            user=request.user, is_default=True
        ).first(),
        "counties": UserAddress.COUNTIES,
    }

    return render(request, "checkout/checkout.html", context)


def checkout_change_address(request):
    addresses = UserAddress.objects.filter(user=request.user)
    # IF CANCEL BUTTON PRESSED
    if request.META.get("HTTP_ACTION") == "CANCEL":
        prev_selected_address_id = request.GET.get("prev_selected_address_id")
        prev_selected_address = UserAddress.objects.get(id=prev_selected_address_id)
        return render(
            request,
            "partials/_shipping-address-widget.html",
            {"default_address": prev_selected_address, "addresses": addresses},
        )
    # IF APPLY BUTTON CLICKED AND NEW ADDRESS CHOSEN
    if request.method == "POST":
        selected_address_id = request.POST.get("address")
        selected_address = UserAddress.objects.get(id=selected_address_id)
        return render(
            request,
            "partials/_shipping-address-widget.html",
            {"default_address": selected_address, "addresses": addresses},
        )
    context = {
        "addresses": addresses,
        "prev_selected_address_id": request.GET.get("prev_selected_address_id"),
    }
    return render(request, "partials/_change-shipping-address-widget.html", context)


def create_payment_intent(request):
    cart = Cart.objects.get(user=request.user)
    amount = cart.get_total_price()
    items_dict = json.dumps(cart.as_dict())
    print(items_dict)
    try:
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=round(amount * 100),
            currency="eur",
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                "enabled": True,
            },
            metadata={
                "email": request.user.email,
                "order_id": uuid.uuid4(),
                "items": items_dict,
                "address": "",
            },
        )
        return JsonResponse({"intent": intent})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=403)


def add_payment_intent_address(request):
    data = json.loads(request.body.decode("utf-8"))
    print(f"REQUEST BODY {data}")

    # Check if both 'client_secret' and 'address' are present in the data
    client_secret = data.get("client_secret")
    address_id = data.get("address")
    intent_id = data.get("intent_id")
    print(client_secret)
    print(address_id)
    payment_intent = stripe.PaymentIntent.retrieve(intent_id)
    payment_intent.metadata.address = address_id
    stripe.PaymentIntent.modify(intent_id, metadata=payment_intent.metadata)

    print("ADDRESS ADDED TO META")
    print(payment_intent.metadata)
    return HttpResponse("")


def checkout_confirmation_view(request):
    payment_intent_client_secret = request.GET.get("payment_intent_client_secret")
    payment_intent = request.GET.get("payment_intent")
    payment_intent = stripe.PaymentIntent.retrieve(payment_intent)
    order_id = payment_intent.get("metadata").get("order_id")
    cart = Cart.objects.get(user=request.user)
    cart.delete()
    context = {
        "order_id": order_id,
        "status": payment_intent.get("status"),
    }

    return render(request, "checkout/confirmation.html", context)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None
    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event
    if event.type == "payment_intent.succeeded":
        payment_intent = event.data.object
        print(payment_intent)
        print(payment_intent.get("metadata"))
        order_items = json.loads(payment_intent.get("metadata").get("items"))
        customer_email = payment_intent.get("metadata").get("email")
        order_id = payment_intent.get("metadata").get("order_id")
        address_id = payment_intent.get("metadata").get("address")
        print(f"THIS IS THE ADDRESS {address_id}")
        print(f"THIS IS THE ORDER {order_id}")
        order_address = OrderAddress.create_from_user_address(
            order=None, user_address=UserAddress.objects.get(id=address_id)
        )
        order_address.save()
        order = Order.objects.create(
            order_id=order_id,
            user=User.objects.get(email=customer_email),
            email=customer_email,
            address=order_address,
        )
        order.save()
        order_address.order = order
        order_address.save()
        for item in order_items.get("items", []):
            order_item = OrderItem.objects.create(
                order=order,
                item=ProductVariant.objects.get(id=item.get("item")),
                quantity=item.get("quantity"),
                price=item.get("quantity")
                * ProductVariant.objects.get(id=item.get("item")).product.get_price(),
            )
            order_item.save()

    elif event.type == "payment_method.attached":
        payment_method = event.data.object
    else:
        print("Unhandled event type {}".format(event.type))

    return HttpResponse(status=200)
