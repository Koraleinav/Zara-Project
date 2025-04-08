# This file will be seedding the db with default products with every migration

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from product.models import Product

@receiver(post_migrate)
def seed_product_data(sender, **kwargs):
    if sender.name == "product" and not Product.objects.exists():
        call_command('seed_products')
