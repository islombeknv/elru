from django.db.models.signals import pre_save
from django.dispatch import receiver

from books.models import BookModel


@receiver(pre_save, sender=BookModel)
def update_price(sender, instance, *args, **kwargs):
    if instance.paper_disc():
        instance.paper_dic_price = instance.paper_price - instance.paper_price * instance.paper_discount / 100
    else:
        instance.paper_dic_price = instance.paper_price


@receiver(pre_save, sender=BookModel)
def update_audio_price(sender, instance, *args, **kwargs):
    if instance.audio_disc():
        instance.audio_dic_price = instance.audio_price - instance.audio_price * instance.audio_discount / 100
    else:
        instance.audio_dic_price = instance.audio_price


@receiver(pre_save, sender=BookModel)
def update_pdf_price(sender, instance, *args, **kwargs):
    if instance.pdf_disc():
        instance.pdf_dic_price = instance.pdf_price - instance.pdf_price * instance.pdf_discount / 100
    else:
        instance.pdf_dic_price = instance.pdf_price
