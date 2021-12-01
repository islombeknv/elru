from django.urls import path

from api.views import *

app_name = 'api'

urlpatterns = [
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
