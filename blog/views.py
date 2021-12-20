from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from blog.models import PostModel
from blog.serializers import PostModelSerializer


class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.order_by('-pk')


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAdminUser]


class PostUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAdminUser]


class PostDelateAPIView(DestroyAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAdminUser]


class PostRetrieveAPIView(RetrieveAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
