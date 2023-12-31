from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    category = serializers.CharField()