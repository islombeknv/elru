from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response


from accounts.serializers import CreateUserProfileSerializer, UserProfileSerializer, PasswordSerializer

UserModel = get_user_model()


class RegistrationAPI(GenericAPIView):
    serializer_class = CreateUserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UserListAPIView(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = self.request.GET.get('user')
        qs = UserModel.objects.all()
        if user:
            qs = qs.filter(username=user)
        return qs


class ChangePasUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PasswordSerializer
    queryset = UserModel.objects.all()


@api_view(['POST'])
@login_required(login_url='/auth/login/')
def DeleteAccount(request):
    UserModel.objects.get(username=request.user).delete()
    return Response(status=status.HTTP_200_OK)

