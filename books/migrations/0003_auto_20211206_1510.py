# Generated by Django 3.2.8 on 2021-12-06 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_authormodal'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='PublisherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publisher',
            },
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='languages',
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='publication_date',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='languages',
            field=models.ManyToManyField(to='books.LanguageModel'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.publishermodel'),
        ),
    ]