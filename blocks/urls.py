from django.urls import path

from blocks.views import *

urlpatterns = [
    path('mainbanner/', MainBannerListAPIView.as_view()),
    path('mainbanner/create/', MainBannerCreateAPIView.as_view()),
    path('mainbanner/update/<int:pk>/', MainBannerUpdateAPIView.as_view()),
    path('mainbanner/delete/<int:pk>/', MainBannerDelateAPIView.as_view()),

    path('collection/', CollectionCollectionListAPIView.as_view()),
    path('collection/create/', CollectionCreateAPIView.as_view()),
    path('collection/update/<int:pk>/', CollectionUpdateAPIView.as_view()),
    path('collection/delete/<int:pk>/', CollectionDelateAPIView.as_view()),

    path('top100/', Top100BookListAPIView.as_view()),
    path('top100/create/', Top100BookCreateAPIView.as_view()),
    path('top100/update/<int:pk>/', Top100BookUpdateAPIView.as_view()),
    path('top100/delete/<int:pk>/', Top100BookDelateAPIView.as_view()),

    path('monthbook/', MonthBookListAPIView.as_view()),
    path('monthbook/create/', MonthBookCreateAPIView.as_view()),
    path('monthbook/update/<int:pk>/', MonthBookUpdateAPIView.as_view()),
    path('monthbook/delete/<int:pk>/', MonthBookDelateAPIView.as_view()),

    path('network/', NetworkListAPIView.as_view()),
    path('network/create/', NetworkCreateAPIView.as_view()),
    path('network/update/<int:pk>/', NetworkUpdateAPIView.as_view()),
    path('network/delete/<int:pk>/', NetworkDelateAPIView.as_view()),
]
