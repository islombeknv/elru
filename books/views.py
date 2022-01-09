from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from books.serializers import *
import pytz
from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, get_object_or_404

today = datetime.now(pytz.timezone('Asia/Tashkent'))


class LanguageListAPIView(ListAPIView):
    serializer_class = LanguageModelSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs.get('q')
        if pk:
            return LanguageModel.objects.filter(id=pk)
        return LanguageModel.objects.order_by('-pk')


class LanguageCreateAPIView(CreateAPIView):
    serializer_class = LanguageModelSerializer
    queryset = LanguageModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class LanguageUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = LanguageModelSerializer
    queryset = LanguageModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@login_required
def LanguageDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        LanguageModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


# ------------------------------------------------------------------------
class PublisherListAPIView(ListAPIView):
    serializer_class = PublisherModelSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.request.GET.get('q')
        if pk:
            return PublisherModel.objects.filter(id=pk)
        return PublisherModel.objects.order_by('-pk')


class PublisherCreateAPIView(CreateAPIView):
    serializer_class = PublisherModelSerializer
    queryset = PublisherModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class PublisherUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PublisherModelSerializer
    queryset = PublisherModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@login_required
def PublisherDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        PublisherModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


# ------------------------------------------------------------------------
class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorModalSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.request.GET.get('q')
        if pk:
            return AuthorModal.objects.filter(id=pk)
        return AuthorModal.objects.order_by('-pk')


class AuthorCreateAPIView(CreateAPIView):
    serializer_class = AuthorModalSerializer
    queryset = AuthorModal.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class AuthorUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AuthorModalSerializer
    queryset = AuthorModal.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@login_required
def AuthorDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        AuthorModal.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


# ------------------------------------------------------------------------
class BookListAPIView(ListAPIView):  # user uchun
    serializer_class = BookModelSerializer
    queryset = BookModel.objects.order_by('-pk')

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
                           Q(title_en__icontains=q) |
                           Q(author__name__icontains=q)
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


class AdminBookListAPIView(ListAPIView):
    serializer_class = BookModelSerializer
    permission_classes = [IsAdminUser]

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


class BookRelatedListView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        return BookModel.objects.filter(category_id=self.kwargs.get('pk'))


class BookCreateAPIView(CreateAPIView):
    serializer_class = AdminBookModelSerializer
    queryset = BookModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AdminBookModelSerializer
    queryset = BookModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
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
        if pk:
            return BookModel.objects.filter(category__id=pk)
        return BookModel.objects.order_by('-pk')


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def CategoryDelateAPIView(request):
    tab = request.GET.getlist('option')
    for i in tab:
        CategoryModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = ProfileModel.objects.get(user=request.user)
        book = BookModel.objects.get(id=self.kwargs.get('pk'))
        comment = self.request.POST.get('comment')
        CommentModel.objects.create(user=user, book=book, comment=comment)
        return Response(status=status.HTTP_201_CREATED)


class CommmentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        book = BookModel.objects.get(id=self.kwargs.get('pk'))
        return CommentModel.objects.filter(book=book)


class AdmCommentListSerializer(ListAPIView):
    serializer_class = AdminCommentListSerializer

    def get_queryset(self):
        return AdminCommentModel.objects.filter(com_id=self.kwargs.get('pk'))


class AdminCommentCreateAPIView(CreateAPIView):
    serializer_class = ReplyCreateSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        text = self.request.POST.get('text')
        com = CommentModel.objects.get(id=self.kwargs.get('pk'))
        user = UserModel.objects.get(username=request.user)
        AdminCommentModel.objects.create(com=com, user=user, text=text)
        return Response(status=status.HTTP_201_CREATED)
