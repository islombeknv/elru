from rest_framework import serializers

from blog.models import PostModel, Image


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        exclude = ['title', 'info', 'content']


class ImageSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.FileField(max_length=100000,
                                                               allow_empty_file=False,
                                                               use_url=False))

    class Meta:
        model = Image
        fields = '__all__'
