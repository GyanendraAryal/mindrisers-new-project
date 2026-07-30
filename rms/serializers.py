from rest_framework import serializers
from .models import Category, Table, Menu, OrderMenu


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(name=validated_data.get("name"))

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class TableSerializer(serializers.Serializer):
    num = serializers.CharField()
    is_available = serializers.BooleanField()

    def create(self, validated_data):
        return Table.objects.create(
            is_available=validated_data.get("is_available"),
            num=validated_data.get("num"),
        )

    def update(self, instance, validated_data):
        instance.is_available = validated_data.get(
            "is_available", instance.is_available
        )
        instance.num = validated_data.get("num", instance.num)
        instance.save()
        return instance


class MenuSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    price = serializers.FloatField()
    image = serializers.ImageField()
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return {"id": obj.category.id, "name": obj.category.name}
