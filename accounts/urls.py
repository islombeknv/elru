from django.urls import path

from accounts.views import RegistrationAPI, UserListAPIView, \
    ChangePasUpdateAPIView, DeleteAccount, ProfileAPIView

urlpatterns = [
    path('create/', RegistrationAPI.as_view()),
    path('list/', UserListAPIView.as_view()),
    path('change/password/<int:pk>/', ChangePasUpdateAPIView.as_view()),
    path('delete/account/', DeleteAccount),
    path('profile/', ProfileAPIView.as_view()),
]
