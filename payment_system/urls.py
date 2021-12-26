from django.urls import path
from payment_system.click import ClickTransaction
from payment_system.payme import PayMeView

app_name = 'payment-system'
urlpatterns = [
    path('click/', ClickTransaction.as_view()),
    path('payme/', PayMeView.as_view()),

]
