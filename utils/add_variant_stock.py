from core.models import *
import random


variants = ProductVariant.objects.all()
quantity_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
weights = [25, 35, 45, 55, 65, 75, 85, 95, 100, 105, 110, 115, 120, 125, 130, 135]

for variant in variants:
    variant.quantity = random.choices(quantity_choices, cum_weights=weights, k=1)[0]
    variant.save()
