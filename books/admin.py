from django.contrib import admin

from books.models import BookModel, CategoryModel, FormatModel

admin.site.register(FormatModel)
admin.site.register(BookModel)
admin.site.register(CategoryModel)
