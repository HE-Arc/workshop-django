from django.contrib.auth.models import User
from django.db import models

# TODO-1-0 Créer un nouveau model nommé CaffeineItem et ajouter
# les champs : name, description, serving_size_in_ml, caffeine_amount_in_mg, created, updated
# class CaffeineItem(models.Model):
#   name = models.CharField(max_length=100)
#   ...


class CaffeineItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    serving_size_in_ml = models.FloatField()
    caffeine_amount_in_mg = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# TODO-1-1 Créer une nouvelle migration et l'appliquer


# TODO-6-0 Créer un nouveau model nommé ConsumedItem et ajouter
# les champs : user, caffeine_item, consumed_number, consumption_date, created, updated


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
    consumption_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# TODO-6-1 Créer une nouvelle migration et l'appliquer
