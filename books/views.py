from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import pytz
from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, get_object_or_404

from accounts.serializers import UserProfileSerializer
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


class LanguageUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = LanguageModelSerializer
    queryset = LanguageModel.objects.order_by('-pk')


@api_view(['GET', 'POST'])
def LanguageDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        LanguageModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


# ------------------------------------------------------------------------
class PublisherListAPIView(ListAPIView):
    serializer_class = PublisherModelSerializer

    def get_queryset(self):
        pk = self.request.GET.get('q')
        if pk:
            return PublisherModel.objects.filter(id=pk)
        return PublisherModel.objects.order_by('-pk')


class PublisherCreateAPIView(CreateAPIView):
    serializer_class = PublisherModelSerializer
    queryset = PublisherModel.objects.order_by('-pk')


class PublisherUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PublisherModelSerializer
    queryset = PublisherModel.objects.order_by('-pk')


@api_view(['GET', 'POST'])
def PublisherDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        PublisherModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


# ------------------------------------------------------------------------
class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorModalSerializer

    def get_queryset(self):
        pk = self.request.GET.get('q')
        if pk:
            return AuthorModal.objects.filter(id=pk)
        return AuthorModal.objects.order_by('-pk')


class AuthorCreateAPIView(CreateAPIView):
    serializer_class = AuthorModalSerializer
    queryset = AuthorModal.objects.order_by('-pk')


class AuthorUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AuthorModalSerializer
    queryset = AuthorModal.objects.order_by('-pk')


@api_view(['GET', 'POST'])
def AuthorDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        AuthorModal.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


# ------------------------------------------------------------------------
class BookListAPIView(ListAPIView):  # 1 oylik top kitoblar
    serializer_class = BookModelSerializer
    queryset = BookModel.objects.filter(created_at__month=today.month).order_by('-book_view')


class AdminBookListAPIView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        q = self.request.GET.get('q')
        aut = self.request.GET.get('aut')
        cat = self.request.GET.get('cat')
        num = self.request.GET.get('num')
        form = self.request.GET.get('form')
        tip = self.request.GET.get('tip')
        qs = BookModel.objects.all()
        if q:
            qs = qs.filter(Q(title_uz__icontains=q) |
                           Q(title_ru__icontains=q) |
                           Q(title_en__icontains=q)
                           )
        if aut:
            qs = qs.filter(author__name__icontains=aut)
        if cat:
            qs = qs.filter(category__title__icontains=cat)
        if num:
            qs = qs.filter(print_length=num)
        if form:
            qs = qs.filter(form__icontains=form)
        if tip:
            qs = qs.filter(tip__icontains=tip)
        return qs


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


# class BookRelatedListView(ListAPIView):
#     serializer_class = BookModelSerializer
#
#     def get_queryset(self):
#         book = BookModel.objects.filter(id=self.kwargs.get('pk')).values('category')
#         print(book.strip('['))
#         # return BookModel.objects.filter(category_id=self.category_id).exclude(pk=self.pk)


class BookCreateAPIView(CreateAPIView):
    serializer_class = AdminBookModelSerializer
    queryset = BookModel.objects.order_by('-pk')


class BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AdminBookModelSerializer
    queryset = BookModel.objects.order_by('-pk')


@api_view(['GET', 'POST'])
def BookDelateAPIView(request):
    tab = request.GET.getlist('option')
    print(tab)
    for i in tab:
        BookModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


# ------------------------------------------------------------------------
class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')

    def get_queryset(self):
        pk = self.request.GET.get('q')
        if pk:
            return CategoryModel.objects.filter(id=pk)
        return CategoryModel.objects.order_by('-pk')


class CategoryRetrieveAPIViewAPIView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        print(pk)
        if pk:
            return BookModel.objects.filter(category_id=pk)
        return BookModel.objects.order_by('-pk')


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')


@api_view(['GET', 'POST'])
def CategoryDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        CategoryModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentModelSerializer

    def create(self, request, *args, **kwargs):
        user = UserModel.objects.get(username=request.user)
        book = BookModel.objects.get(id=self.kwargs.get('pk'))
        comment = self.request.POST.get('comment')
        CommentModel.objects.create(user=user, book=book, comment=comment)
        return Response(status=status.HTTP_200_OK)


class CommmentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        book = BookModel.objects.get(id=self.kwargs.get('pk'))
        return CommentModel.objects.filter(book=book)


class CommmentAouthorListAPIView(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserModel.objects.filter(id=self.kwargs.get('pk'))
