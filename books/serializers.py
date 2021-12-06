from rest_framework import serializers
from books.models import CategoryModel, BookModel, FormatModel


class FormatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatModel
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['created_at', 'updated_at']


class BookModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    format = FormatModelSerializer()

    class Meta:
        model = BookModel
        exclude = ['created_at', 'updated_at']


class BookModelUpdateSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    format = FormatModelSerializer()

    class Meta:
        model = BookModel
        exclude = ['book_view', 'created_at', 'updated_at']
