from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

from accounts.models import ProfileModel

UserModel = get_user_model()


@receiver(pre_save, sender=UserModel)
def accounts(sender, instance, *args, **kwargs):
    z
