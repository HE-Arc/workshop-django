from django.db import models

# TODO-1-0 Créer un nouveau model nommé CaffeineItem et ajouter
# les champs : name, description, serving_size_in_ml, caffeine_amount_in_mg, created, updated
class CaffeineItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=2000, blank=True)
  serving_size_in_ml = models.FloatField()
  caffeine_amount_in_ml = models.FloatField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
# TODO-1-1 Créer une nouvelle migration et l'appliquer

# TODO-6-0 Créer un nouveau model nommé ConsumedItem et ajouter
# les champs : user, caffeine_item, consumed_number, consumption_date, created, updated
# TODO-6-1 Créer une nouvelle migration et l'appliquer
