import many
from rest_framework import serializers

from accounts.serializers import UserProfile2Serializer
from books.models import *


class LanguageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        exclude = ['created_at', 'updated_at']


class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        exclude = ['created_at', 'updated_at', 'title']


class AuthorModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModal
        exclude = ['created_at', 'updated_at', 'name']


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['created_at', 'updated_at', 'title']


class BookModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(many=True)
    publisher = PublisherModelSerializer()
    author = AuthorModalSerializer()
    languages = LanguageModelSerializer(many=True)

    class Meta:
        model = BookModel
        exclude = ['created_at', 'updated_at', 'book_view',
                   'title', 'description', 'audio_file', 'pdf_file']


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
    user = UserProfile2Serializer()

    class Meta:
        model = CommentModel
        fields = '__all__'


class AdminCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminCommentModel
        fields = '__all__'


class ReplyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminCommentModel
        fields = ['text']
