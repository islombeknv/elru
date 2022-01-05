# Generated by Django 3.2.8 on 2022-01-04 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default=orders.models.create_new_ref_number, max_length=10, unique=True)),
                ('book', models.JSONField()),
                ('territory', models.CharField(max_length=100)),
                ('city_district', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('full_name', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('status', models.CharField(blank=True, choices=[('Kutilmoqda', 'Kutilmoqda'), ('Tasdiqlandi', 'Tasdiqlandi'), ('Yuborildi', 'Yuborildi'), ('Yetkazildi', 'Yetkazildi')], default='Kutilmoqda', max_length=100, null=True)),
                ('pay', models.CharField(choices=[('progress', 'progress'), ('click', 'click'), ('payme', 'payme')], default='progress', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
