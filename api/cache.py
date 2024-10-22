from django.core.cache import cache
from .models import Order

class Caching:
    # caching of all models that are transferred 
    @staticmethod
    def get_base_model(key, obj):
        key = key
        cached_data = cache.get(key)

        if cached_data is None:
            cached_data = obj.objects.all()

        cache.set(key, cached_data, timeout=24 * 60 * 60)

        return cached_data
    
    # caching a model on a specific user
    @staticmethod
    def cache_orders_for_user(user_id):
        key = f"orders_{user_id}"
        cached_data = cache.get(key)

        if cached_data is None:
            cached_data = Order.objects.filter(user__id = user_id)

        cache.set(key, cached_data, timeout=24 * 60 * 60)

        return cached_data
    