from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    
# This line tells Django to use your custom AppConfig (in apps.py) instead of the default. And in apps.py, you import your signals:
    def ready(self):
        import product.signals
