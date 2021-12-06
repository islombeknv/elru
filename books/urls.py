from django.urls import path

from books.views import *

app_name = ''

urlpatterns = [
    path('languages/', LanguageListAPIView.as_view()),
    path('language/create/', LanguageCreateAPIView.as_view()),
    path('language/update/<int:pk>/', LanguageUpdateAPIView.as_view()),
    path('language/delate/<int:pk>/', LanguageDelateAPIView.as_view()),

    path('publishers/', PublisherListAPIView.as_view()),
    path('publisher/create/', PublisherCreateAPIView.as_view()),
    path('publisher/update/<int:pk>/', PublisherUpdateAPIView.as_view()),
    path('publisher/delate/<int:pk>/', PublisherDelateAPIView.as_view()),

    path('author/', AuthorListAPIView.as_view()),
    path('author/create/', AuthorCreateAPIView.as_view()),
    path('author/update/<int:pk>/', AuthorUpdateAPIView.as_view()),
    path('author/delate/<int:pk>/', AuthorDelateAPIView.as_view()),

    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookRetrieveAPIView.as_view()),
    path('books/create/', BookCreateAPIView.as_view()),
    path('books/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('books/delate/<int:pk>/', BookDelateAPIView.as_view()),

    path('category/', CategoryListAPIView.as_view()),
    path('category/create/', CategoryCreateAPIView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view()),
    path('category/delate/<int:pk>/', CategoryDelateAPIView.as_view()),

    path('format/list/', FormatListAPIView.as_view()),
    path('format/create/', FormatCreateAPIView.as_view()),
    path('format/update/<int:pk>/', FormatUpdateAPIView.as_view()),
    path('format/delate/<int:pk>/', FormatDelateAPIView.as_view()),

]
