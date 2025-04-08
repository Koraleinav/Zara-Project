from django.core.management.base import BaseCommand
from product.models import Product
from category.models import Category
from django.core.files import File
import os

class Command(BaseCommand):
    help = "Seed products to the db"

    def handle(self, *args, **kwargs):
        product_1 = Product.objects.create(
            name='Applique T-Shirt',
            price=19.99,
            status='IN_STOCK',
            picture='products/applique_t-shirt.jpg',
            quantity=100
        )
        product_1.category.add(
            Category.objects.get(type="SHIRT", gender="FEMALE", season="SUMMER", collection="CASUAL")
        )

        product_2 = Product.objects.create(
            name='Blue Jeans',
            price=29.99,
            status='IN_STOCK',
            picture='products/blue_jeans.jpg',
            quantity=100
        )
        product_2.category.add(
            Category.objects.get(type="PANTS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_3 = Product.objects.create(
            name='Boots for Girls - Black',
            price=49.99,
            status='IN_STOCK',
            picture='products/boots_for_girls_-_black.jpg',
            quantity=100
        )
        product_3.category.add(
            Category.objects.get(type="SHOES", gender="KIDS", season="FALL", collection="CASUAL")
        )

        product_4 = Product.objects.create(
            name='Cropped Shirt with Pocket',
            price=24.99,
            status='IN_STOCK',
            picture='products/cropped_shirt_with_pocket.jpg',
            quantity=100
        )
        product_4.category.add(
            Category.objects.get(type="SHIRT", gender="FEMALE", season="SUMMER", collection="CASUAL")
        )

        product_5 = Product.objects.create(
            name='Denim Cargo Parachute - Ecru',
            price=39.99,
            status='IN_STOCK',
            picture='products/denim_cargo_parachute_-_ecru.jpg',
            quantity=100
        )
        product_5.category.add(
            Category.objects.get(type="PANTS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_6 = Product.objects.create(
            name='Draped Neck Dress',
            price=59.99,
            status='IN_STOCK',
            picture='products/draped_neck_dress.jpg',
            quantity=100
        )
        product_6.category.add(
            Category.objects.get(type="DRESS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_7 = Product.objects.create(
            name='Girls Winter Boots',
            price=29.99,
            status='IN_STOCK',
            picture='products/girls_winter_boots.jpg',
            quantity=100
        )
        product_7.category.add(
            Category.objects.get(type="SHOES", gender="KIDS", season="FALL", collection="CASUAL")
        )

        product_8 = Product.objects.create(
            name='Heart Denim Pants - Mid Blue',
            price=39.99,
            status='IN_STOCK',
            picture='products/heart_denim_pants_-_mid_blue.jpg',
            quantity=100
        )
        product_8.category.add(
            Category.objects.get(type="PANTS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_9 = Product.objects.create(
            name='High-rise Long Length Straight Cut Jeans - Light Blue',
            price=25.99,
            status='IN_STOCK',
            picture='products/high-rise_long_length_straight_cut_jeans_-_light_blue.jpg',
            quantity=100
        )
        product_9.category.add(
            Category.objects.get(type="PANTS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_10 = Product.objects.create(
            name='High-waist Barrel Leg Jeans - Mid Blue',
            price=35.99,
            status='IN_STOCK',
            picture='products/high-waist_barrel_leg_jeans_-_mid_blue.jpg',
            quantity=100
        )
        product_10.category.add(
            Category.objects.get(type="PANTS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_11 = Product.objects.create(
            name='Metallic Shirt',
            price=49.99,
            status='IN_STOCK',
            picture='products/metallic_shirt.jpg',
            quantity=100
        )
        product_11.category.add(
            Category.objects.get(type="SHIRT", gender="FEMALE", season="SUMMER", collection="CASUAL")
        )

        product_12 = Product.objects.create(
            name='Regualt White T-Shirt',
            price=19.99,
            status='IN_STOCK',
            picture='products/regualt white t-shirt.webp',
            quantity=100
        )
        product_12.category.add(
            Category.objects.get(type="SHIRT", gender="FEMALE", season="SUMMER", collection="CASUAL")
        )

        product_13 = Product.objects.create(
            name='Ripped Skinny Jeans - Blue',
            price=24.99,
            status='IN_STOCK',
            picture='products/ripped_skinney_jeans_-_blue.jpg',
            quantity=100
        )
        product_13.category.add(
            Category.objects.get(type="PANTS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_14 = Product.objects.create(
            name='Satin Dress with Sequins',
            price=59.99,
            status='IN_STOCK',
            picture='products/satin_dress_with_sequans.jpg',
            quantity=100
        )
        product_14.category.add(
            Category.objects.get(type="DRESS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_15 = Product.objects.create(
            name='Short Printed Dress',
            price=34.99,
            status='IN_STOCK',
            picture='products/short printed dress.jpg',
            quantity=100
        )
        product_15.category.add(
            Category.objects.get(type="DRESS", gender="FEMALE", season="SUMMER", collection="EVENING")
        )

        product_16 = Product.objects.create(
            name='Short Textured Dress',
            price=27.99,
            status='IN_STOCK',
            picture='products/short_textured_dress.jpg',
            quantity=100
        )
        product_16.category.add(
            Category.objects.get(type="DRESS", gender="FEMALE", season="SUMMER", collection="EVENING")
        )

        product_17 = Product.objects.create(
            name='Straight Fit Cargo Jeans - Light Blue',
            price=29.99,
            status='IN_STOCK',
            picture='products/straight_fit_cargo_jeans_-_light_blue.jpg',
            quantity=100
        )
        product_17.category.add(
            Category.objects.get(type="PANTS", gender="FEMALE", season="WINTER", collection="EVENING")
        )

        product_18 = Product.objects.create(
            name='Striped Crochet Shirt - Black & White',
            price=45.99,
            status='IN_STOCK',
            picture='products/striped_crochet_shirt_-_black_N_white.jpg',
            quantity=100
        )
        product_18.category.add(
            Category.objects.get(type="SHIRT", gender="FEMALE", season="SUMMER", collection="CASUAL")
        )

        product_19 = Product.objects.create(
            name='Sweatshirt - Purple',
            price=34.99,
            status='IN_STOCK',
            picture='products/sweatshirt__-_purple.jpg',
            quantity=100
        )
        product_19.category.add(
            Category.objects.get(type="SHIRT", gender="FEMALE", season="WINTER", collection="CASUAL")
        )

        product_20 = Product.objects.create(
            name='Textured Shirt - White',
            price=29.99,
            status='IN_STOCK',
            picture='products/textured_shirt_-_white.jpg',
            quantity=100
        )
        product_20.category.add(
            Category.objects.get(type="SHIRT", gender="FEMALE", season="SUMMER", collection="CASUAL")
        )

        self.stdout.write(self.style.SUCCESS('Successfully created products.'))
