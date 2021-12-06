from rest_framework import serializers

from blog.models import PostModel


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


