# Generated by Django 3.2.8 on 2021-11-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_bookmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='book_view',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
