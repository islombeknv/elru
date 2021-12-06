from django.urls import path

from accounts.views import UserListAPIView

urlpatterns = [
    path('list/', UserListAPIView.as_view()),
]
