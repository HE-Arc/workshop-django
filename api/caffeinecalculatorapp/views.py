from functools import partial
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import CaffeineItem, ConsumedItem
from .serializers import (
    CaffeineItemSerializer,
    ComplexeUserSerializer,
    ConsumedItemSerializer,
    UserSerializer,
)


# NOTE: Endpoint for the root of our API
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "consumed-items": reverse(
                "consumeditem-list", request=request, format=format
            ),
            "caffeine-items": reverse(
                "caffeineitem-list", request=request, format=format
            ),
        }
    )


# # NOTE: function-based view
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


# @api_view(["GET", "PUT", "DELETE"])
# def caffeine_item_detail(request, pk):
#     try:
#         caffeine_item = CaffeineItem.objects.get(pk=pk)
#     except CaffeineItem.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = CaffeineItemSerializer(caffeine_item)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = CaffeineItemSerializer(caffeine_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         caffeine_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # NOTE: class-based view
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


# class CaffeineItemDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return CaffeineItem.objects.get(pk=pk)
#         except CaffeineItem.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         caffeine_item = self.get_object(pk)
#         serializer = CaffeineItemSerializer(caffeine_item)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         caffeine_item = self.get_object(pk)
#         serializer = CaffeineItemSerializer(caffeine_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         caffeine_item = self.get_object(pk)
#         caffeine_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # NOTE: class-based view using mixins
# class CaffeineItemList(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     queryset = CaffeineItem.objects.all()
#     serializer_class = CaffeineItemSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class CaffeineItemDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = CaffeineItem.objects.all()
#     serializer_class = CaffeineItemSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# # NOTE: generic class-based view
# class CaffeineItemList(generics.ListCreateAPIView):
#     queryset = CaffeineItem.objects.all()
#     serializer_class = CaffeineItemSerializer


# class CaffeineItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CaffeineItem.objects.all()
#     serializer_class = CaffeineItemSerializer


# class ConsumedItemList(generics.ListCreateAPIView):
#     queryset = ConsumedItem.objects.all()
#     serializer_class = ConsumedItemSerializer

#     # NOTE: Overrides the perform_create function comming from mixins.CreateModelMixin
#     # which generics.ListCreateAPIView inherits
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class ConsumedItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ConsumedItem.objects.all()
#     serializer_class = ConsumedItemSerializer


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = ComplexeUserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = ComplexeUserSerializer


# NOTE: ViewSets instead of views
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConsumedItemViewSet(viewsets.ModelViewSet):
    queryset = ConsumedItem.objects.all()
    serializer_class = ConsumedItemSerializer

    @action(
        detail=True, methods=["POST"], url_path="increase-first-caffeine-item-by-one"
    )
    def increase_first_caffeine_item_by_one(self, request, pk):
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

    # NOTE: Overrides the perform_create function comming from mixins.CreateModelMixin
    # which generics.ListCreateAPIView inherits
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CaffeineItemViewSet(viewsets.ModelViewSet):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer
