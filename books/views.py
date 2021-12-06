from rest_framework.response import Response
from datetime import datetime
import pytz
from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    DestroyAPIView, get_object_or_404
from books.serializers import *
from books.models import *

today = datetime.now(pytz.timezone('Asia/Tashkent'))


class LanguageListAPIView(ListAPIView):
    serializer_class = LanguageModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('q')
        if pk:
            return LanguageModel.objects.filter(id=pk)
        return LanguageModel.objects.order_by('-pk')


class LanguageCreateAPIView(CreateAPIView):
    serializer_class = LanguageModelSerializer
    queryset = LanguageModel.objects.order_by('-pk')


class LanguageDelateAPIView(DestroyAPIView):
    serializer_class = LanguageModelSerializer
    queryset = LanguageModel.objects.order_by('-pk')


class LanguageUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = LanguageModelSerializer
    queryset = LanguageModel.objects.order_by('-pk')


# ------------------------------------------------------------------------
class PublisherListAPIView(ListAPIView):
    serializer_class = PublisherModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('q')
        if pk:
            return PublisherModel.objects.filter(id=pk)
        return PublisherModel.objects.order_by('-pk')


class PublisherCreateAPIView(CreateAPIView):
    serializer_class = PublisherModelSerializer
    queryset = PublisherModel.objects.order_by('-pk')


class PublisherDelateAPIView(DestroyAPIView):
    serializer_class = PublisherModelSerializer
    queryset = PublisherModel.objects.order_by('-pk')


class PublisherUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PublisherModelSerializer
    queryset = PublisherModel.objects.order_by('-pk')


# ------------------------------------------------------------------------
class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorModalSerializer

    def get_queryset(self):
        pk = self.kwargs.get('q')
        if pk:
            return AuthorModal.objects.filter(id=pk)
        return AuthorModal.objects.order_by('-pk')


class AuthorCreateAPIView(CreateAPIView):
    serializer_class = AuthorModalSerializer
    queryset = AuthorModal.objects.order_by('-pk')


class AuthorDelateAPIView(DestroyAPIView):
    serializer_class = AuthorModalSerializer
    queryset = AuthorModal.objects.order_by('-pk')


class AuthorUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AuthorModalSerializer
    queryset = AuthorModal.objects.order_by('-pk')


# ------------------------------------------------------------------------
class BookListAPIView(ListAPIView):  # 1 oylik top kitoblar
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


# ------------------------------------------------------------------------
class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')

    def get_queryset(self):
        pk = self.kwargs.get('q')
        if pk:
            return CategoryModel.objects.filter(id=pk)
        return CategoryModel.objects.order_by('-pk')


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


class CategoryDelateAPIView(DestroyAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


# ------------------------------------------------------------------------
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
