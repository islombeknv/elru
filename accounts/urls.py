from django.urls import path

from accounts.views import RegistrationAPI

urlpatterns = [
    path('create/', RegistrationAPI.as_view()),
]
