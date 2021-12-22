from clickuz import ClickUz
from django.http import HttpResponseNotFound
from paycomuz import Paycom
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.utils import json

from accounts.models import ProfileModel
from accounts.serializers import UserProfile2Serializer
from books.models import BookModel
from orders.models import OrderModel, UserModel
from orders.serializers import OrderModelSerializer, OrderListSerializer, \
    OrderPdfBookModel, OrderAudioBookModel, OrderENDListSerializer


class OrderCreateView(CreateAPIView):
    serializer_class = OrderModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        book = json.loads(self.request.POST.get('book'))
        price = 0
        qs = BookModel.objects.all()
        for i in book[0]['book']:
            if i['format'] == 'pdf' and qs.filter(id=i['id']):
                pdf = qs.filter(id=i['id']).values('pdf_dic_price')
                price += pdf[0]['pdf_dic_price']
            elif i['format'] == 'paper' and qs.filter(id=i['id']):
                pdf = qs.filter(id=i['id']).values('paper_dic_price')
                price += pdf[0]['paper_dic_price'] * i['count']
            elif i['format'] == 'audio' and qs.filter(id=i['id']):
                pdf = qs.filter(id=i['id']).values('audio_dic_price')
                price += pdf[0]['audio_dic_price']
            else:
                price = 0
        user = UserModel.objects.get(username=request.user)
        territory = self.request.POST.get('territory')
        city_district = self.request.POST.get('city_district')
        address = self.request.POST.get('address')
        full_name = self.request.POST.get('full_name')
        note = self.request.POST.get('note')
        phone = self.request.POST.get('phone')
        order = OrderModel.objects.create(user=user, book=book, territory=territory,
                                          city_district=city_district, address=address,
                                          full_name=full_name, note=note, phone=phone, price=price)

        # paycom = Paycom()
        # url = paycom.create_initialization(amount=order.price, order_id=order.order_id, return_url='https://elru.cf')
        url = ClickUz.generate_url(amount=order.price, order_id=order.order_id, return_url='http://example.com')
        return Response(url, status=status.HTTP_201_CREATED)


class OrderListView(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        order_id = self.request.GET.get('q')
        status = self.request.GET.get('status')
        print(status)
        from_date = self.request.GET.get('from_date')
        to_date = self.request.GET.get('to_date')
        if order_id:
            return OrderModel.objects.filter(order_id=order_id)
        elif from_date and to_date:
            return OrderModel.objects.filter(
                created_at__range=(f"{from_date.replace('/', '-')} 00:00:00",
                                   f"{to_date.replace('/', '-')} 00:00:00"))
        elif status:
            return OrderModel.objects.filter(status=status)

        return OrderModel.objects.order_by('-pk')


class OrderRetrieveAPIView(RetrieveAPIView):
    serializer_class = OrderListSerializer
    queryset = OrderModel.objects.all()
    permission_classes = [IsAdminUser]


class OrderEndAPIView(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = UserModel.objects.all()
        return OrderModel.objects.filter(user__in=user)


class OrderEndRetrieveAPIView(ListAPIView):
    serializer_class = OrderENDListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user = UserModel.objects.filter(id=pk)[0]
        return OrderModel.objects.filter(user=user)


class MyOrderListView(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserModel.objects.get(username=self.request.user)
        if user:
            return OrderModel.objects.filter(user=user)
        return Response('empty_response')


class MyOrderPDFListView(ListAPIView):
    serializer_class = OrderPdfBookModel
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        order = OrderModel.objects.filter(user=self.request.user).values('book')
        if order:
            book = order[0]['book'][0]['book']
            for i in book:
                if pk == i['id'] and i['format'] == 'pdf':
                    return BookModel.objects.filter(id=pk)

        return HttpResponseNotFound("not found")


class MyOrderAudioListView(ListAPIView):
    serializer_class = OrderAudioBookModel
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        order = OrderModel.objects.filter(user=self.request.user).values('book')
        if order:
            book = order[0]['book'][0]['book']
            for i in book:
                if pk == i['id'] and i['format'] == 'audio':
                    return BookModel.objects.filter(id=pk)

        return HttpResponseNotFound("not found")


class AdminUserOrderAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfile2Serializer
    permission_classes = [IsAdminUser]

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        user = UserModel.objects.filter(id=pk)[0]
        profile, _ = ProfileModel.objects.get_or_create(user=user)
        return profile
