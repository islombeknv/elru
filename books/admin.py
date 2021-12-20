from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from books.models import BookModel, CategoryModel, \
    AuthorModal, LanguageModel, PublisherModel, CommentModel, AdminCommentModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BookModel)
class BookModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'author', 'category', 'created_at']
    list_filter = ['title', 'category', 'author', 'created_at']
    search_fields = ['languages', 'publisher', 'author', 'category']
    readonly_fields = ['paper_dic_price', 'audio_dic_price', 'pdf_dic_price', ]
    autocomplete_fields = ["category", "author", "publisher", "languages"]


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(AuthorModal)
class AuthorModalAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(PublisherModel)
class PublisherModelAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(LanguageModel)
class PublisherModelAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(CommentModel)
admin.site.register(AdminCommentModel)
