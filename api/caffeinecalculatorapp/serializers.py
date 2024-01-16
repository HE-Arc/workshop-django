from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CaffeineItem, ConsumedItem

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
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField(required=False, max_length=2000)
#     serving_size_in_ml = serializers.FloatField()
#     caffeine_amount_in_mg = serializers.FloatField()

#     def create(self, validated_data):
#         return CaffeineItem.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.serving_size_in_ml = validated_data.get(
#             "serving_size_in_ml", instance.serving_size_in_ml
#         )
#         instance.caffeine_amount_in_mg = validated_data.get(
#             "caffeine_amount_in_mg", instance.caffeine_amount_in_mg
#         )
#         instance.save()
#         return instance

# TODO-3-1 Réécrire le serializer en héritant de HyperlinkedModelSerializer
class CaffeineItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaffeineItem
        fields = [
            "url",
            "id",
            "name",
            "description",
            "serving_size_in_ml",
            "caffeine_amount_in_mg",
        ]

# TODO-6-2 Créer un nouveau serializer pour le ConsumedItem

class ConsumedItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConsumedItem
        fields = [
            "url",
            "id",
            "user",
            "caffeine_item",
            "consumed_number",
            "consumption_date",
        ]

# TODO-6-9 Créer un nouveau serializer héritant de User qui possède davantage de champs (FK)
class ComplexUserSerializer(UserSerializer):
    consumed_items = serializers.HyperlinkedRelatedField(
        many=True, view_name="consumeditem-detail", read_only=True
    )

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + [
            "consumed_items",
        ]

# TODO-6-11 Créer un nouveau serializer héritant de ConsumedItem qui possède davantage de champs (FK)
class ComplexConsumedItemSerializer(ConsumedItemSerializer):
    user_obj = UserSerializer(source="user", read_only=True)
    caffeine_item_obj = CaffeineItemSerializer(source="caffeine_item", read_only=True)

    class Meta:
        model = ConsumedItem
        fields = ConsumedItemSerializer.Meta.fields + [
            "user_obj",
            "caffeine_item_obj",
        ]