from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class LanguageModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class PublisherModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publisher'


class AuthorModal(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class FormatModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'format'
        verbose_name_plural = 'format'


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BookModel(models.Model):
    category = models.ForeignKey(CategoryModel, related_name='books', on_delete=models.PROTECT, )
    format = models.ForeignKey(FormatModel, on_delete=models.CASCADE, related_name='book')

    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    real_price = models.FloatField(default=0, blank=True)

    publisher = models.ForeignKey(PublisherModel, on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField()
    print_length = models.IntegerField()
    languages = models.ManyToManyField(LanguageModel, )
    discount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    book_view = models.IntegerField(default=0, blank=True)

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        else:
            return self.price

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
