from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.helpers import modify_input_for_multiple_files
from blog.models import PostModel, Image
from blog.serializers import PostModelSerializer, ImageSerializer


class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.order_by('-pk')


class PostCreateAPIView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser,)
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


class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(img_name)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)
