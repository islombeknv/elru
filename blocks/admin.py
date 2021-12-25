from django.contrib import admin

from blocks.models import MainBannerModal, NetworkModal, \
    CollectionModel, Top100BookModel, MonthBookModel, ApplicationsModel


@admin.register(MainBannerModal)
class MainBannerModalAdmin(admin.ModelAdmin):
    list_display = ['link1', 'created_at']
    search_fields = ['link1', 'created_at']
    list_filter = ['created_at']


@admin.register(CollectionModel)
class CollectionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['created_at']


@admin.register(Top100BookModel)
class Top100BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['created_at']


@admin.register(MonthBookModel)
class MonthBookModelAdmin(admin.ModelAdmin):
    list_display = ['link', 'created_at']
    search_fields = ['link', 'created_at']
    list_filter = ['created_at']


@admin.register(NetworkModal)
class NetworkModalAdmin(admin.ModelAdmin):
    list_display = ['instagram', 'telegram', 'facebook', 'created_at']
    search_fields = ['instagram', 'telegram', 'facebook']
    list_filter = ['created_at']


@admin.register(ApplicationsModel)
class NetworkModalAdmin(admin.ModelAdmin):
    list_display = ['number', 'created_at']
    search_fields = ['number']
    list_filter = ['created_at']