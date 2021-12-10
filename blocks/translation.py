from modeltranslation.translator import register, TranslationOptions

from blocks.models import CollectionModel, Top100BookModel


@register(CollectionModel)
class PostModelTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Top100BookModel)
class PostModelTranslationOptions(TranslationOptions):
    fields = ['title', 'content']