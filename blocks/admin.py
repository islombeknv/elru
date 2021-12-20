from django.contrib import admin

from blocks.models import MainBannerModal, NetworkModal, \
    CollectionModel, Top100BookModel, MonthBookModel, ApplicationsModel

admin.site.register(MainBannerModal)
admin.site.register(CollectionModel)
admin.site.register(Top100BookModel)
admin.site.register(MonthBookModel)
admin.site.register(NetworkModal)
admin.site.register(ApplicationsModel)

