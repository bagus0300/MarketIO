from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from core.models import Cart, ProductVariant
from users.models import UserAddress, User
from .models import Order, OrderItem, OrderAddress
import stripe
import json
import uuid


@login_required
def checkout_view(request):
    """
    View function for the checkout page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered checkout page.
    """
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
    """
    View function for handling the change of shipping address during checkout.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
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
    """
    Create a payment intent for the user's cart.

    Args:
        request: The HTTP request object.

    Returns:
        A JSON response containing the payment intent if successful, or an error message if unsuccessful.
    """
    cart = Cart.objects.get(user=request.user)
    amount = cart.get_total_price()
    items_dict = json.dumps(cart.as_dict())
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
    """
    Add the address to the metadata of a payment intent.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: An empty HTTP response.
    """
    data = json.loads(request.body.decode("utf-8"))
    # Check if both 'client_secret' and 'address' are present in the data
    client_secret = data.get("client_secret")
    address_id = data.get("address")
    intent_id = data.get("intent_id")
    payment_intent = stripe.PaymentIntent.retrieve(intent_id)
    payment_intent.metadata.address = address_id
    stripe.PaymentIntent.modify(intent_id, metadata=payment_intent.metadata)
    return HttpResponse("")


def checkout_confirmation_view(request):
    """
    Renders the checkout confirmation page with the order details.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered confirmation page.
    """
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
    """
    Handle Stripe webhook events.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
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
        order_items = json.loads(payment_intent.get("metadata").get("items"))
        customer_email = payment_intent.get("metadata").get("email")
        order_id = payment_intent.get("metadata").get("order_id")
        address_id = payment_intent.get("metadata").get("address")
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
