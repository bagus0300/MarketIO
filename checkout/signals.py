from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.models import Order


@receiver(pre_save, sender=Order)
def set_order_id(sender, instance, **kwargs):
    """
    Signal receiver function that sets the order_id for the Order model instance.

    Args:
        sender: The sender of the signal.
        instance: The instance of the Order model being saved.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if not instance.order_id:
        instance.order_id = Order.generate_order_id()
