from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from blocks.models import MainBannerModal, CollectionModel, Top100BookModel, MonthBookModel, NetworkModal, \
    ApplicationsModel
from blocks.serializers import MainBannerModalSerializer, CollectionModelSerializer, Top100BookModelSerializer, \
    MonthBookModelSerializer, NetworkModalSerializer, ApplicationsModelSerializer


class MainBannerListAPIView(ListAPIView):
    serializer_class = MainBannerModalSerializer
    queryset = MainBannerModal.objects.order_by('-pk')


class MainBannerCreateAPIView(CreateAPIView):
    serializer_class = MainBannerModalSerializer
    queryset = MainBannerModal.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class MainBannerUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MainBannerModalSerializer
    queryset = MainBannerModal.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def MainBannerDelateAPIView(request):
    tab = request.GET.getlist('d')
    for i in tab:
        MainBannerModal.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class CollectionCollectionListAPIView(ListAPIView):
    serializer_class = CollectionModelSerializer
    queryset = CollectionModel.objects.order_by('-pk')


class CollectionCreateAPIView(CreateAPIView):
    serializer_class = CollectionModelSerializer
    queryset = CollectionModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class CollectionUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CollectionModelSerializer
    queryset = CollectionModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def CollectionDelateAPIView(request):
    tab = request.GET.getlist('d')
    for i in tab:
        CollectionModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class Top100BookListAPIView(ListAPIView):
    serializer_class = Top100BookModelSerializer
    queryset = Top100BookModel.objects.order_by('-pk')


class Top100BookCreateAPIView(CreateAPIView):
    serializer_class = Top100BookModelSerializer
    queryset = Top100BookModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class Top100BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = Top100BookModelSerializer
    queryset = Top100BookModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def Top100BookDelateAPIView(request):
    tab = request.GET.getlist('d')
    for i in tab:
        Top100BookModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class MonthBookListAPIView(ListAPIView):
    serializer_class = MonthBookModelSerializer
    queryset = MonthBookModel.objects.order_by('-pk')


class MonthBookCreateAPIView(CreateAPIView):
    serializer_class = MonthBookModelSerializer
    queryset = MonthBookModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class MonthBookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MonthBookModelSerializer
    queryset = MonthBookModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def MonthBookDelateAPIView(request):
    tab = request.GET.getlist('d')
    for i in tab:
        MonthBookModel.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class NetworkListAPIView(ListAPIView):
    serializer_class = NetworkModalSerializer
    queryset = NetworkModal.objects.order_by('-pk')


class NetworkCreateAPIView(CreateAPIView):
    serializer_class = NetworkModalSerializer
    queryset = NetworkModal.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


class NetworkUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = NetworkModalSerializer
    queryset = NetworkModal.objects.order_by('-pk')
    permission_classes = [IsAdminUser]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def NetworkDelateAPIView(request):
    tab = request.GET.getlist('d')
    for i in tab:
        NetworkModal.objects.get(id=i).delete()
    return Response(status=status.HTTP_200_OK)


class ApplicationsListAPIView(ListAPIView):
    serializer_class = ApplicationsModelSerializer
    queryset = ApplicationsModel.objects.order_by('-pk')


class ApplicationsCreateAPIView(CreateAPIView):
    serializer_class = ApplicationsModelSerializer
    queryset = ApplicationsModel.objects.order_by('-pk')
    permission_classes = [IsAdminUser]
