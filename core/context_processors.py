from core.models import Cart

def cart_quantity_badge(request):
    """ 
    This context processor adds the cart quantity to the navbar.
    """
    cart_total_quantity=0
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
        cart_total_quantity = cart.get_total_items()
        print(cart_total_quantity)
    context = {
        "cart_total_quantity":cart_total_quantity,
    }
    return context