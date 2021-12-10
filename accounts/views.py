from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from accounts.models import ProfileModel
from accounts.serializers import CreateUserProfileSerializer


class RegistrationAPI(GenericAPIView):
    serializer_class = CreateUserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = ProfileModel.objects.create(user=self.request.POST.get('username'))
        return Response(data, status=status.HTTP_200_OK)