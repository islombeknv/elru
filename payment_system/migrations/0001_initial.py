# Generated by Django 3.1.2 on 2021-05-14 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewClickTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_trans_id', models.CharField(max_length=255)),
                ('merchant_trans_id', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
                ('sign_string', models.CharField(max_length=255)),
                ('sign_datetime', models.DateTimeField(max_length=255)),
                ('status', models.CharField(choices=[('processing', 'processing'), ('finished', 'finished'), ('canceled', 'canceled')], default='processing', max_length=25)),
            ],
            options={
                'verbose_name': 'Click новый Транзакция ',
                'verbose_name_plural': 'Click новый Транзакция ',
                'db_table': 'new_click_transaction_uz',
            },
        ),
    ]