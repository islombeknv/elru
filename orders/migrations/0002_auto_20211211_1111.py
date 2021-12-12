# Generated by Django 3.2.8 on 2021-12-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='country',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='city_district',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='full_name',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='locality',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='note',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='territory',
            field=models.CharField(default=5, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='address1',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='postcode',
            field=models.CharField(max_length=50),
        ),
    ]