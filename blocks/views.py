from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from blocks.models import MainBannerModal, CollectionModel, Top100BookModel, MonthBookModel, NetworkModal
from blocks.serializers import MainBannerModalSerializer, CollectionModelSerializer, Top100BookModelSerializer, \
    MonthBookModelSerializer, NetworkModalSerializer


class MainBannerListAPIView(ListAPIView):
    serializer_class = MainBannerModalSerializer
    queryset = MainBannerModal.objects.order_by('-pk')


class MainBannerCreateAPIView(CreateAPIView):
    serializer_class = MainBannerModalSerializer
    queryset = MainBannerModal.objects.order_by('-pk')


class MainBannerUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MainBannerModalSerializer
    queryset = MainBannerModal.objects.order_by('-pk')


class MainBannerDelateAPIView(DestroyAPIView):
    serializer_class = MainBannerModalSerializer
    queryset = MainBannerModal.objects.order_by('-pk')


class CollectionCollectionListAPIView(ListAPIView):
    serializer_class = CollectionModelSerializer
    queryset = CollectionModel.objects.order_by('-pk')


class CollectionCreateAPIView(CreateAPIView):
    serializer_class = CollectionModelSerializer
    queryset = CollectionModel.objects.order_by('-pk')


class CollectionUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CollectionModelSerializer
    queryset = CollectionModel.objects.order_by('-pk')


class CollectionDelateAPIView(DestroyAPIView):
    serializer_class = CollectionModelSerializer
    queryset = CollectionModel.objects.order_by('-pk')


class Top100BookListAPIView(ListAPIView):
    serializer_class = Top100BookModelSerializer
    queryset = Top100BookModel.objects.order_by('-pk')


class Top100BookCreateAPIView(CreateAPIView):
    serializer_class = Top100BookModelSerializer
    queryset = Top100BookModel.objects.order_by('-pk')


class Top100BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = Top100BookModelSerializer
    queryset = Top100BookModel.objects.order_by('-pk')


class Top100BookDelateAPIView(DestroyAPIView):
    serializer_class = Top100BookModelSerializer
    queryset = Top100BookModel.objects.order_by('-pk')


class MonthBookListAPIView(ListAPIView):
    serializer_class = MonthBookModelSerializer
    queryset = MonthBookModel.objects.order_by('-pk')


class MonthBookCreateAPIView(CreateAPIView):
    serializer_class = MonthBookModelSerializer
    queryset = MonthBookModel.objects.order_by('-pk')


class MonthBookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MonthBookModelSerializer
    queryset = MonthBookModel.objects.order_by('-pk')


class MonthBookDelateAPIView(DestroyAPIView):
    serializer_class = MonthBookModelSerializer
    queryset = MonthBookModel.objects.order_by('-pk')


class NetworkListAPIView(ListAPIView):
    serializer_class = NetworkModalSerializer
    queryset = NetworkModal.objects.order_by('-pk')


class NetworkCreateAPIView(CreateAPIView):
    serializer_class = NetworkModalSerializer
    queryset = NetworkModal.objects.order_by('-pk')


class NetworkUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = NetworkModalSerializer
    queryset = NetworkModal.objects.order_by('-pk')


class NetworkDelateAPIView(DestroyAPIView):
    serializer_class = NetworkModalSerializer
    queryset = NetworkModal.objects.order_by('-pk')
