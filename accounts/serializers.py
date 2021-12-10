from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class CreateUserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        return Response(user, status=status.HTTP_200_OK)
