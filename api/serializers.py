from rest_framework import serializers

from books.models import CategoryModel, BookModel, FormatModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['created_at', 'updated_at']


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        exclude = ['created_at', 'updated_at']


class BookModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        exclude = ['book_view', 'created_at', 'updated_at']


class FormatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatModel
        fields = '__all__'