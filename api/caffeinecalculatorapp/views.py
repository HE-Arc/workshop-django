from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

# TODO-1-6 Créer des nouvelles views pour le User (décommenter simplement ce code, plus de détails après)
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# TODO-3-2 Créer des nouvelles views en function-based pour le CaffeineItem
# TODO-3-3 Réécrire les views en class-based
# TODO-3-4 Réécrire les views en utilisant les mixins
# TODO-3-5 Réécrire les views en utilisant les generics
# TODO-3-6 Réécrire les views en utilisant les viewsets

# TODO-6-3 Créer une nouvelle viewset pour le ConsumedItem et lui ajouter une
# action POST permettant d'incrémenter le consumed number d'un consumed item
# TODO-6-6 Remplacer les generic views du User par un viewset
# TODO-6-10 Mettre à jour le viewset du User pour utiliser le nouveau serializer
# TODO-6-12 Mettre à jour le viewset de ConsumedItem pour utiliser le nouveau serializer
# et vérifier que les nouvelles données sont bien accessibles via la browsable API de DRF
