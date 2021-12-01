from django.db.models.signals import pre_save
from django.dispatch import receiver

from books.models import BookModel


@receiver(pre_save, sender=BookModel)
def update_price(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.real_price = instance.price - instance.price * instance.discount / 100
    else:
        instance.real_price = instance.price