from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.models import Order


@receiver(pre_save, sender=Order)
def set_order_id(sender, instance, **kwargs):
    if not instance.order_id:
        instance.order_id = Order.generate_order_id()
