from accounts.serializers import UserProfileSerializer
from books.serializers import *
from orders.models import OrderModel


class OrderPdfBookModel(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['pdf_file']


class OrderAudioBookModel(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['audio_file']


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        exclude = ['created_at', 'user', 'price', 'status', 'order_id', 'pay']


class OrderListSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderENDListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModel
        fields = ['order_id',]
