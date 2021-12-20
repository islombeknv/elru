from django.db import models


class MainBannerModal(models.Model):
    banner1 = models.ImageField(upload_to='banner')
    link1 = models.CharField(max_length=100)
    banner2 = models.ImageField(upload_to='banner')
    link2 = models.CharField(max_length=100)
    banner3 = models.ImageField(upload_to='banner')
    link3 = models.CharField(max_length=100)

    small_banner1 = models.ImageField(upload_to='banner')
    small_link1 = models.CharField(max_length=100)
    small_banner2 = models.ImageField(upload_to='banner')
    small_link2 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link1

    class Meta:
        verbose_name = 'mainbanner'
        verbose_name_plural = 'mainbanner'


class CollectionModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='collection')
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'collection'
        verbose_name_plural = 'collections'


class Top100BookModel(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='top100book')
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'top100book'
        verbose_name_plural = 'top100books'


class MonthBookModel(models.Model):
    image = models.ImageField(upload_to='monthbook')
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'monthbook'
        verbose_name_plural = 'monthbooks'


class NetworkModal(models.Model):
    instagram = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instagram

    class Meta:
        verbose_name = 'network'
        verbose_name_plural = 'networks'


class ApplicationsModel(models.Model):
    number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'