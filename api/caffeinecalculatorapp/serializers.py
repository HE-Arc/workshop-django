from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CaffeineItem, ConsumedItem

# # NOTE: Default way of writing a serializer
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


# # NOTE: Refactored using ModelSerializer
# class CaffeineItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CaffeineItem
#         fields = [
#             "id",
#             "name",
#             "description",
#             "serving_size_in_ml",
#             "caffeine_amount_in_mg",
#         ]


# NOTE: Refactored using HyperlinkedModelSerializer
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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
        ]


# NOTE: More complexe serializer for users including additionnal fields
# Keeping a "default" serializer with the default fields representation
# also avoids circular calls
# e.g.: UserSerializer fetches the consumed_items using the ConsumedItemSerializer
# which fetches the user using the UserSerializer, etc. (it never ends until it crashes)
class ComplexeUserSerializer(UserSerializer):
    # # NOTE: Reverse relationship, not included by default
    # consumed_items = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=ConsumedItem.objects.all()
    # )

    consumed_items = serializers.HyperlinkedRelatedField(
        many=True, view_name="consumeditem-detail", read_only=True
    )
    # consume_items =

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + [
            "consumed_items",
        ]


class ConsumedItemSerializer(serializers.HyperlinkedModelSerializer):
    # NOTE: it's possible to display anything else, here we display the username instead of the ID
    # user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = ConsumedItem
        fields = [
            "url",
            "id",
            "user",
            "caffeine_item",
            "consumed_number",
            "created",
        ]


class ComplexeConsumedItemSerializer(ConsumedItemSerializer):
    user_obj = UserSerializer(source="user", read_only=True)
    caffeine_item_obj = CaffeineItemSerializer(source="caffeine_item", read_only=True)

    class Meta:
        model = ConsumedItem
        fields = ConsumedItemSerializer.Meta.fields + [
            "user_obj",
            "caffeine_item_obj",
        ]
