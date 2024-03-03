from rest_framework import serializers

from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'year']


    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['orders_count'] = ...
    #     return representation


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = ['user_name', 'days_count', 'date']


    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['books'] = ...
    #     return representation
