from modeltranslation.translator import register, TranslationOptions

from books.models import PublisherModel, AuthorModal, CategoryModel, BookModel


@register(PublisherModel)
class PublisherTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(AuthorModal)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BookModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
