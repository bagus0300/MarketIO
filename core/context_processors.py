from core.models import Cart


def cart_quantity_badge(request):
    """
    This context processor adds the cart quantity to the navbar.
    Uses users saved cart if authenticated, otherwise uses session cart.
    If Anon user logs in, cart items are added to User cart.
    """

    cart_total_quantity = 0
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
        print(request.session.session_key)
        if Cart.objects.filter(session=request.session.session_key):
            session_cart = Cart.objects.filter(session=request.session.session_key)[0]
            for item in session_cart.cartitem_set.all():
                item.cart = cart
                item.save()

    elif request.user.is_anonymous:
        if request.session.session_key is None:
            request.session.save()

        cart = Cart.objects.get_or_create(session=request.session.session_key)[0]

    cart_total_quantity = cart.get_total_items()

    context = {
        "cart_total_quantity": cart_total_quantity,
        "cart": cart,
    }
    return context
