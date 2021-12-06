from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import ProfileModel
from accounts.serializers import ProfileModalSerializer


class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileModalSerializer

    def get_queryset(self):
        return ProfileModel.objects.filter(user=self.request.user)
