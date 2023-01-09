from django.contrib.auth.models import User
from django.db import models


class CaffeineItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    serving_size_in_ml = models.FloatField()
    caffeine_amount_in_mg = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ConsumedItem(models.Model):
    user = models.ForeignKey(
        User, related_name="consumed_items", on_delete=models.CASCADE
    )
    caffeine_item = models.ForeignKey(
        CaffeineItem,
        related_name="consumed_items",
        on_delete=models.SET_NULL,
        null=True,
    )
    consumed_number = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
