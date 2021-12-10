from rest_framework import serializers
from blocks.models import MainBannerModal, CollectionModel, Top100BookModel, MonthBookModel, NetworkModal


class MainBannerModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBannerModal
        exclude = ['created_at']


class CollectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionModel
        exclude = ['created_at', 'title']


class Top100BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top100BookModel
        exclude = ['created_at', 'title', 'content']


class MonthBookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthBookModel
        exclude = ['created_at']


class NetworkModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkModal
        exclude = ['created_at']
