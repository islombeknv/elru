from rest_framework import serializers

from blog.models import PostModel, Image


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        exclude = ['title', 'info', 'content']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

