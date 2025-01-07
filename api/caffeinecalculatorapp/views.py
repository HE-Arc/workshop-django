from .serializers import ComplexeConsumedItemSerializer
from .serializers import ComplexeUserSerializer
from .models import ConsumedItem
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from .serializers import ConsumedItemSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer, CaffeineItemSerializer
from .models import CaffeineItem
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
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


@api_view(["GET", "POST"])
def caffeine_item_list(request):
    if request.method == "GET":
        caffeine_items = CaffeineItem.objects.all()
        serializer = CaffeineItemSerializer(caffeine_items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CaffeineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO-3-3 Réécrire les views en class-based


class CaffeineItemList(APIView):
    def get(self, request, format=None):
        caffeine_items = CaffeineItem.objects.all()
        serializer = CaffeineItemSerializer(caffeine_items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CaffeineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO-3-4 Réécrire les views en utilisant les mixins


class CaffeineItemList(APIView):
    def get(self, request, format=None):
        caffeine_items = CaffeineItem.objects.all()
        serializer = CaffeineItemSerializer(caffeine_items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CaffeineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO-3-5 Réécrire les views en utilisant les generics


class CaffeineItemList(generics.ListCreateAPIView):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer

# TODO-3-6 Réécrire les views en utilisant les viewsets


class CaffeineItemViewSet(viewsets.ModelViewSet):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer

# TODO-6-3 Créer une nouvelle viewset pour le ConsumedItem et lui ajouter une
# action POST permettant d'incrémenter le consumed number d'un consumed item


class ConsumedItemViewSet(viewsets.ModelViewSet):
    queryset = ConsumedItem.objects.all()
    serializer_class = ConsumedItemSerializer

    @action(detail=True, methods=["POST"], url_path="increase-by-one")
    def increase_by_one(self, request, pk):
        consumed_item = get_object_or_404(ConsumedItem, pk=pk)

        data = {"consumed_number": consumed_item.consumed_number + 1}
        serializer = self.get_serializer(
            consumed_item,
            data=data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO-6-6 Remplacer les generic views du User par un viewset
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# TODO-6-10 Mettre à jour le viewset du User pour utiliser le nouveau serializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = ComplexeUserSerializer

# TODO-6-12 Mettre à jour le viewset de ConsumedItem pour utiliser le nouveau serializer
# et vérifier que les nouvelles données sont bien accessibles via la browsable API de DRF


class ConsumedItemViewSet(viewsets.ModelViewSet):
    queryset = ConsumedItem.objects.all()
    serializer_class = ComplexeConsumedItemSerializer


...
