from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from blog.models import PostModel
from blog.serializers import PostModelSerializer


class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.order_by('-pk')


class PostCreateAPIView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PostModelSerializer
    permission_classes = [IsAdminUser]


class PostUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAdminUser]


class PostDelateAPIView(DestroyAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def PostDelateAPIView(request):
    tab = request.GET.getlist('d')
    for i in tab:
        PostModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class PostRetrieveAPIView(RetrieveAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
