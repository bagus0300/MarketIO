from django.shortcuts import render
from products.models import ProductVariant
from django.http import HttpResponse
from .models import Cart, CartItem

def add_to_cart(request):
    """
    Add a product to the cart.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the cart counter badge.
    """
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
    """
    Remove an item from the cart.

    Args:
        request (HttpRequest): The HTTP request object.
        cart_item_id (int): The ID of the cart item to be removed.

    Returns:
        HttpResponse: The HTTP response containing the updated cart information.
    """
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
    """
    Update the quantity of a cart item and return the updated cart information.

    Args:
        request (HttpRequest): The HTTP request object.
        cart_item_id (int): The ID of the cart item to update.
        quantity (int): The new quantity value.

    Returns:
        HttpResponse: The HTTP response containing the updated cart information.
    """
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart = cart_item.cart
    cart_item.quantity = quantity
    cart_item.save()
    cart.save()
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
    """
    View function for displaying the cart.

    If the user is authenticated, the function retrieves the cart associated with the user.
    Otherwise, it retrieves the cart associated with the session.

    Returns:
        A rendered HTML template displaying the cart items and cart details.
    """
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