from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView

from blog.models import PostModel
from blog.serializers import PostModelSerializer


class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.order_by('-pk')


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()


class PostUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()


class PostDelateAPIView(DestroyAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()


class PostRetrieveAPIView(RetrieveAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
