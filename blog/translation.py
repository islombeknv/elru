from modeltranslation.translator import register, TranslationOptions

from blog.models import PostModel


@register(PostModel)
class PublisherTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'content')
