from django.db import models
from users.models import Address


class OrderItem(models.Model):
    """
    Represents an item in an order.

    Attributes:
        order (Order): The order to which this item belongs.
        item (ProductVariant): The product variant associated with this item.
        quantity (int): The quantity of this item in the order.
        price (Decimal): The price of this item.
    """
    order = models.ForeignKey("checkout.Order", on_delete=models.CASCADE)
    item = models.ForeignKey("core.ProductVariant", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)


class Order(models.Model):
    """
    Represents an order made by a user.

    Attributes:
        order_id (str): The ID of the order.
        user (User): The user who placed the order.
        address (OrderAddress): The address associated with the order.
        email (str): The email address of the user who placed the order.
        date_created (datetime): The date and time when the order was created.
    """

    order_id = models.CharField()
    user = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)
    address = models.ForeignKey(
        "checkout.OrderAddress", on_delete=models.DO_NOTHING, related_name="order_address"
    )
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        """
        Calculates and returns the total price of the order.

        Returns:
            float: The total price of the order.
        """
        order_items = self.orderitem_set.all()
        total = 0
        for item in order_items:
            total += item.price * item.quantity
        return total


class OrderAddress(Address):
    """
    Represents an address associated with an order.

    Inherits from the Address class.

    Attributes:
        order (Order): The order associated with the address.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    @classmethod
    def create_from_user_address(cls, order, user_address):
        """
        Creates an OrderAddress instance from a user address.

        Args:
            order (Order): The order associated with the address.
            user_address (UserAddress): The user address to create the OrderAddress from.

        Returns:
            OrderAddress: The created OrderAddress instance.
        """
        return cls(
            order=order,
            user=user_address.user,
            name=user_address.name,
            address_line_1=user_address.address_line_1,
            address_line_2=user_address.address_line_2,
            city=user_address.city,
            county=user_address.county,
            eircode=user_address.eircode,
        )
