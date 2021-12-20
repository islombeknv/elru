from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from accounts.models import ProfileModel

User = get_user_model()


class CreateUserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        return Response(user, status=status.HTTP_200_OK)


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_superuser',
                   'is_staff', 'groups', 'user_permissions']


class UserProfile2Serializer(ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = ProfileModel
        fields = '__all__'


class PasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'password'
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
