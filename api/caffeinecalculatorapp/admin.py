from django.contrib import admin
from caffeinecalculatorapp.models import CaffeineItem

# TODO-1-2 Importer le nouveau model et l'ajouter à l'interface admin de Django
# TODO-1-3 Ajouter un nouvel utilisateur à l'aide de l'interface admin de Django
# TODO-1-4 Ajouter 2 nouveaux caffeine items à l'aide de l'interface admin de Django

admin.site.register(CaffeineItem)