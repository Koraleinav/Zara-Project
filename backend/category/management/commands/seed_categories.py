# This file will be seedding the db with default categorys

from django.core.management.base import BaseCommand
from category.models import Category
from django.core.files import File

class Command(BaseCommand):
    help = "seed categorys to the db"

    def handle(self, *args, **kwargs):
        # Import choices directly from the Category model
        from category.models import TYPE_CHOICES, GENDER_CHOICES, SEASON_CHOICES, COLLECTIONS_CHOICES

        # Loop over all combinations of the choices and create categories
        categories_data = []
        for gender in GENDER_CHOICES:
            for category_type in TYPE_CHOICES:
                for season in SEASON_CHOICES:
                    for collection in COLLECTIONS_CHOICES:
                        category = Category(
                            type=category_type[0],
                            gender=gender[0],
                            season=season[0],
                            collection=collection[0]
                        )
                        categories_data.append(category)
        
        # Save all categories to the database in bulk
        Category.objects.bulk_create(categories_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(categories_data)} categories!'))