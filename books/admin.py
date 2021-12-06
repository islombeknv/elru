from django.contrib import admin

from books.models import BookModel, CategoryModel, FormatModel, AuthorModal, LanguageModel

admin.site.register(FormatModel)
admin.site.register(BookModel)
admin.site.register(CategoryModel)
admin.site.register(AuthorModal)
admin.site.register(LanguageModel)
