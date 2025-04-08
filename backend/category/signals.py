# This file will be seedding the db with default categorys with every migration
 
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from category.models import Category

@receiver(post_migrate)
def seed_category_data(sender, **kwargs):
    if sender.name == "category" and not Category.objects.exists():
        call_command('seed_categories')
