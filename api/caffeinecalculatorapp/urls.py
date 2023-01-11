from django.urls import path
from . import views

# TODO-3-7 Ajouter les urls pour le CaffeineItem en utilisant le Router de DRF

# TODO-6-4 Ajouter les urls pour le ConsumedItem en utilisant le Router de DRF
# TODO-6-5 Enregistrer 2 entrer de ConsumedItem via la browsable API de DRF,
# en utilisant le POST form /api/consumed-items/
# TODO-6-7 Ajouter les urls pour le User en utilisant le Router de DRF et supprimer les
# anciennes routes
# TODO-6-8 Vérifier que les routes pour les 3 ressources fonctionnent toujours

urlpatterns = [
    # TODO-1-7 Ajouter des urls pour le User (décommenter simplement ce code, plus de détails après)
    path("users/", views.UserList.as_view(), name="user-list"),
    path(
        "users/<int:pk>/",
        views.UserDetail.as_view(),
        name="user-detail",
    ),
]