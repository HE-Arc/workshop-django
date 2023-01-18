from urllib import response
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import CaffeineItemSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets

from .models import CaffeineItem
from .serializers import UserSerializer

# TODO-1-6 Créer des nouvelles views pour le User (décommenter simplement ce code, plus de détails après)
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# TODO-3-2 Créer des nouvelles views en function-based pour le CaffeineItem
# @api_view(["GET", "POST"])
# def caffeine_item_list(request):
#     if request.method == "GET":
#         caffeine_items = CaffeineItem.objects.all()
#         serializer = CaffeineItemSerializer(caffeine_items, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = CaffeineItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO-3-3 Réécrire les views en class-based
# class CaffeineItemList(APIView):
#     def get(self, request, format=None):
#         caffeine_items = CaffeineItem.objects.all()
#         serializer = CaffeineItemSerializer(caffeine_items, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CaffeineItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO-3-4 Réécrire les views en utilisant les mixins
# class CaffeineItemList(mixins.ListModelMixin,
#                        mixins.CreateModelMixin,
#                        generics.GenericAPIView):
#     queryset=CaffeineItem.objects.all()
#     serializer_class=CaffeineItemSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# TODO-3-5 Réécrire les views en utilisant les generics
# class CaffeineItemList(generics.ListCreateAPIView):
#     queryset = CaffeineItem.objects.all()
#     serializer_class = CaffeineItemSerializer


# TODO-3-6 Réécrire les views en utilisant les viewsets
class CaffeineItemViewSet(viewsets.ModelViewSet):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer


# TODO-6-3 Créer une nouvelle viewset pour le ConsumedItem et lui ajouter une
# action POST permettant d'incrémenter le consumed number d'un consumed item
# TODO-6-6 Remplacer les generic views du User par un viewset
# TODO-6-10 Mettre à jour le viewset du User pour utiliser le nouveau serializer
# TODO-6-12 Mettre à jour le viewset de ConsumedItem pour utiliser le nouveau serializer
# et vérifier que les nouvelles données sont bien accessibles via la browsable API de DRF
