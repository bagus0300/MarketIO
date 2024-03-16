from django.db import models


class CartItem(models.Model):
    """
    Represents an item in a cart.

    Attributes:
        item (ProductVariant): The product variant associated with the cart item.
        cart (Cart): The cart that the item belongs to.
        quantity (int): The quantity of the item in the cart.
    """

    item = models.ForeignKey("products.ProductVariant", on_delete=models.CASCADE)
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}no. {self.item.product.name}"


class Cart(models.Model):
    """
    Represents a cart for a user.

    Attributes:
        user (users.User): The user associated with the cart.
        session (str): The session ID associated with the cart.
    """

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    session = models.CharField(max_length=32, default=None, null=True, blank=True)

    def add_item(self, product, quantity):
        """
        Adds an item to the cart.

        Args:
            product: The product to be added.
            quantity (int): The quantity of the product to be added.

        Returns:
            CartItem: The created or updated cart item.
        """
        cart_item = CartItem.objects.filter(item=product, cart=self)
        if cart_item.exists():
            cart_item = cart_item.first()
            cart_item.quantity = cart_item.quantity + quantity
            cart_item.save()
            return
        return CartItem.objects.create(item=product, cart=self, quantity=quantity)

    def remove_item(self, product):
        """
        Removes an item from the cart.

        Args:
            product: The product to be removed.

        Returns:
            None
        """
        return CartItem.objects.get(item=product, cart=self).delete()

    def get_total_items(self):
        """
        Calculates the total quantity of items in the cart.

        Returns:
            int: The total quantity of items in the cart.
        """
        items = self.cartitem_set.all()
        total_quantity = 0
        for item in items:
            total_quantity += item.quantity
        return total_quantity

    def get_total_price(self):
        """
        Calculates the total price of all items in the cart.

        Returns:
            float: The total price of all items in the cart.
        """
        items = self.cartitem_set.all()
        total_price = 0
        for item in items:
            total_price += item.quantity * item.item.product.get_price()
        return total_price

    def as_dict(self):
        """
        Converts the cart to a dictionary representation.

        Returns:
            dict: A dictionary representation of the cart.
        """
        items = {"items": []}
        for item in self.cartitem_set.all():
            item = dict({"item": item.item.id, "quantity": item.quantity})
            items["items"].append(item)
        return items
