from django.urls import path

from orders.views import OrderCreateView, OrderListView, \
    MyOrderListView, MyOrderPDFListView, MyOrderAudioListView, OrderRetrieveAPIView, OrderEndAPIView, \
    OrderEndRetrieveAPIView, AdminUserOrderAPIView

urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path('list/', OrderListView.as_view()),
    path('list/<int:pk>/', OrderRetrieveAPIView.as_view()),
    path('endorder/', OrderEndAPIView.as_view()),
    path('complete/<int:pk>/', OrderEndRetrieveAPIView.as_view()),
    path('user/profile/<int:pk>/', AdminUserOrderAPIView.as_view()),

    path('user/', MyOrderListView.as_view()),
    path('pdf/<int:pk>', MyOrderPDFListView.as_view()),
    path('audio/<int:pk>', MyOrderAudioListView.as_view()),
]
