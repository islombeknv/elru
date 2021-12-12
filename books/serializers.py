from django.contrib.auth import get_user_model
from rest_framework import serializers
from books.models import CategoryModel, BookModel, AuthorModal, LanguageModel, PublisherModel, CommentModel


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


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['created_at', 'updated_at', 'title']


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        exclude = ['created_at', 'updated_at', 'book_view',
                   'title', 'description', 'paper_dic_price', 'audio_dic_price',
                   'pdf_dic_price', ]


class AdminBookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        exclude = ['created_at', 'updated_at', 'book_view',
                   'title', 'description',
                   'paper_dic_price', 'audio_dic_price',
                   'pdf_dic_price',
                   ]


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['comment']


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'
