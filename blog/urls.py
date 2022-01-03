from django.urls import path

from blog.views import PostListAPIView, PostCreateAPIView, PostUpdateAPIView, PostDelateAPIView, PostRetrieveAPIView

app_name = 'news'

urlpatterns = [
    path('', PostListAPIView.as_view()),
    path('detail/<int:pk>/', PostRetrieveAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),
    path('update/<int:pk>/', PostUpdateAPIView.as_view()),
    path('delete/<int:pk>/', PostDelateAPIView.as_view()),
]
