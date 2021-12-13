from django.urls import path

from books.views import *

urlpatterns = [
    path('languages/', LanguageListAPIView.as_view()),
    path('language/create/', LanguageCreateAPIView.as_view()),
    path('language/update/<int:pk>/', LanguageUpdateAPIView.as_view()),
    path('language/delate/', LanguageDelateAPIView),

    path('publishers/', PublisherListAPIView.as_view()),
    path('publisher/create/', PublisherCreateAPIView.as_view()),
    path('publisher/update/<int:pk>/', PublisherUpdateAPIView.as_view()),
    path('publisher/delate/', PublisherDelateAPIView),

    path('author/', AuthorListAPIView.as_view()),
    path('author/create/', AuthorCreateAPIView.as_view()),
    path('author/update/<int:pk>/', AuthorUpdateAPIView.as_view()),
    path('author/delate/', AuthorDelateAPIView),

    path('books/', AdminBookListAPIView.as_view()),
    path('books/<int:pk>/', BookRetrieveAPIView.as_view()),
    path('books/releted/<int:pk>/', BookRelatedListView.as_view()),
    path('books/create/', BookCreateAPIView.as_view()),
    path('books/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('books/delete/', BookDelateAPIView),

    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveAPIViewAPIView.as_view()),
    path('category/create/', CategoryCreateAPIView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view()),
    path('category/delate/', CategoryDelateAPIView),

    path('comment/create/<int:pk>/', CommentCreateAPIView.as_view()),
    path('comment/list/<int:pk>/', CommmentListAPIView.as_view()),



]
