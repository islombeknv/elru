from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import ProfileModel


class ProfileModalSerializer(serializers.ModelSerializer):
    user = get_user_model()

    class Meta:
        model = ProfileModel
        fields = '__all__'
