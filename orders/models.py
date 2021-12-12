from django.contrib.auth import get_user_model
from django.db import models

from books.models import BookModel

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(BookModel, related_name='order')
    phone = models.CharField(max_length=30)
    full_name = models.CharField(max_length=255)
    territory = models.CharField(max_length=100)
    city_district = models.CharField(max_length=100)
    locality = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    address1 = models.CharField(max_length=300)
    note = models.CharField(max_length=300)
    price = models.FloatField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.user)}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
