from rest_framework import serializers

from blog.models import PostModel


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        exclude = ['title', 'info', 'content']

