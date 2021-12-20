from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()
GENDER = (
    ('girl', 'girl'),
    ('boy', 'boy')
)


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    phone = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'profil'
        verbose_name_plural = 'profiles'
