# Generated by Django 3.2.8 on 2021-12-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0003_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
