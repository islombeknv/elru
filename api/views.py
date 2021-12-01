from datetime import datetime

import pytz
from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.response import Response

from api.serializers import BookModelSerializer, CategoryModelSerializer, BookModelUpdateSerializer, \
    FormatModelSerializer
from books.models import BookModel, CategoryModel, FormatModel

today = datetime.now(pytz.timezone('Asia/Tashkent'))


class BookListAPIView(ListAPIView):
    serializer_class = BookModelSerializer
    queryset = BookModel.objects.filter(created_at__month=today.month).order_by('-book_view')


class BookRetrieveAPIView(RetrieveAPIView):
    serializer_class = BookModelSerializer
    queryset = BookModel.objects.order_by('-pk')

    def retrieve(self, request, pk=None):
        queryset = BookModel.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        article.book_view += 1
        article.save()
        serializer = BookModelSerializer(article)
        return Response(serializer.data)


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookModelSerializer
    queryset = BookModel.objects.order_by('-pk')


class BookDelateAPIView(DestroyAPIView):
    serializer_class = BookModelSerializer
    queryset = BookModel.objects.order_by('-pk')


class BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BookModelUpdateSerializer
    queryset = BookModel.objects.order_by('-pk')


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


class CategoryDelateAPIView(DestroyAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


class FormatListAPIView(ListAPIView):
    serializer_class = FormatModelSerializer
    queryset = FormatModel.objects.order_by('-pk')


class FormatCreateAPIView(CreateAPIView):
    serializer_class = FormatModelSerializer
    queryset = FormatModel.objects.order_by('-pk')


class FormatUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = FormatModelSerializer
    queryset = FormatModel.objects.order_by('-pk')


class FormatDelateAPIView(DestroyAPIView):
    serializer_class = FormatModelSerializer
    queryset = FormatModel.objects.order_by('-pk')
