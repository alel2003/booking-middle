from django.core.cache import cache
from django.db.models import Max

from .models import Order, Product


class Caching:
    @staticmethod
    def get_base_model(key, obj: Product | Order):
        """caching of all models that are transferred"""
        cached_data = cache.get(key)
        timestamp_key = f"{key}_timestamp"

        cached_data = cache.get(key)
        cached_timestamp = cache.get(timestamp_key)

        db_timestamp = obj.objects.all().aggregate(
            last_updated=Max("updated_at")
        )["last_updated"]

        if (
            cached_data is None
            or cached_timestamp is None
            or cached_timestamp < db_timestamp
        ):
            db_data = obj.objects.all()
            cache.set(key, db_data, timeout=24 * 60 * 60)
            cache.set(timestamp_key, db_timestamp, timeout=24 * 60 * 60)
            return db_data

        return cached_data

    @staticmethod
    def cache_get_details(key, model_id, obj: Product | Order):
        """caching of the detailed model query"""
        key = f"{key}_{model_id}"
        timestamp_key = f"{key}_{model_id}_timestamp"

        cached_data = cache.get(key)
        cached_timestamp = cache.get(timestamp_key)

        db_timestamp = obj.objects.filter(id=model_id).aggregate(
            last_updated=Max("updated_at")
        )["last_updated"]

        if (
            cached_data is None
            or cached_timestamp is None
            or cached_timestamp < db_timestamp
        ):
            db_data = obj.objects.filter(id=model_id)
            cache.set(key, db_data, timeout=24 * 60 * 60)
            cache.set(timestamp_key, db_timestamp, timeout=24 * 60 * 60)
            return db_data

        return cached_data

    @staticmethod
    def cache_orders_for_user(user_id):
        key = f"orders_{user_id}"
        timestamp_key = f"orders_{user_id}_timestamp"

        cached_data = cache.get(key)
        cached_timestamp = cache.get(timestamp_key)

        db_timestamp = Order.objects.filter(user__id=user_id).aggregate(
            last_updated=Max("updated_at")
        )["last_updated"]

        if (
            cached_data is None
            or cached_timestamp is None
            or cached_timestamp < db_timestamp
        ):
            db_data = Order.objects.filter(user__id=user_id)
            cache.set(key, db_data, timeout=24 * 60 * 60)
            cache.set(timestamp_key, db_timestamp, timeout=24 * 60 * 60)
            return db_data

        return cached_data
