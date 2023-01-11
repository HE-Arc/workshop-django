from rest_framework import serializers
from django.contrib.auth.models import User

# TODO-1-5 Créer un nouveau serializer pour le User (décommenter simplement ce code, plus de détails après)
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
        ]


# TODO-3-0 Créer un nouveau serializer pour le CaffeineItem
# class CaffeineItemSerializer(serializers.Serializer):
#     ...
#     name = serializers.CharField(max_length=100)
#     ...
#
#     def create(self, validated_data):
#         ...
#
#     def update(self, instance, validated_data):
#         ...

# TODO-3-1 Réécrire le serializer en héritant de HyperlinkedModelSerializer

# TODO-6-2 Créer un nouveau serializer pour le ConsumedItem
# TODO-6-9 Créer un nouveau serializer héritant de User qui possède davantage de champs (FK)
# TODO-6-11 Créer un nouveau serializer héritant de ConsumedItem qui possède davantage de champs (FK)
