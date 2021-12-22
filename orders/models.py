from django.contrib.auth import get_user_model
from django.db import models
import random

UserModel = get_user_model()

STATUS = (
    ('1', 'Kutilmoqda'),
    ('2', 'Tasdiqlandi'),
    ('3', 'Yo`lda'),
    ('4', 'Buyurtma yetkazildi'),
)


def create_new_ref_number():
    return str(f'#{random.randint(10000, 99999)}')


class OrderModel(models.Model):
    order_id = models.CharField(max_length=10, blank=True,
                                unique=True, default=create_new_ref_number)
    user = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE)
    book = models.JSONField()
    territory = models.CharField(max_length=100)
    city_district = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    full_name = models.CharField(max_length=255)
    note = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    price = models.FloatField()
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank=True,
                              default='Tasdiqlash jarayonida')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
