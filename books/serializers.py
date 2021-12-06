from rest_framework import serializers
from books.models import CategoryModel, BookModel, FormatModel, AuthorModal, LanguageModel, PublisherModel


class LanguageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = '__all__'


class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        fields = '__all__'


class AuthorModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModal
        fields = '__all__'


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
