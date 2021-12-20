from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from accounts.models import ProfileModel
from accounts.serializers import CreateUserProfileSerializer, UserProfileSerializer, PasswordSerializer, \
    UserProfile2Serializer

UserModel = get_user_model()


class RegistrationAPI(GenericAPIView):
    serializer_class = CreateUserProfileSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UserListAPIView(ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.GET.get('user')
        qs = UserModel.objects.all()
        if user:
            qs = qs.filter(username=user)
        return qs


class ChangePasUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PasswordSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAdminUser]


@api_view(['POST'])
@permission_classes([IsAdminUser])
def DeleteAccount(request):
    UserModel.objects.get(username=request.user).delete()
    return Response(status=status.HTTP_200_OK)


class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfile2Serializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        profile, _ = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile
