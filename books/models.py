from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from multiselectfield import MultiSelectField

from accounts.models import ProfileModel

UserModel = get_user_model()

BFORMAT = (
    ('paper', 'PAPER'),
    ('pdf', 'PDF'),
    ('audio', 'AUDIO'),
)
TIP = (
    ('discount', 'discount'),
    ('bestseller', 'bestseller'),
    ('recommended', 'recommended'),
    ('new', 'new'),
    ('best_prices', 'best_prices'),
)


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
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.CharField(max_length=100)
    publication_date = models.DateField()
    print_length = models.IntegerField()
    languages = models.ManyToManyField(LanguageModel, blank=True)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(AuthorModal, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(CategoryModel, blank=True)
    form = MultiSelectField(choices=BFORMAT)
    tip = MultiSelectField(choices=TIP)
    paper_price = models.FloatField(default=0, null=True, blank=True)
    paper_discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    paper_dic_price = models.FloatField(default=0, null=True, blank=True)
    quantity = models.CharField(max_length=100)

    audio_price = models.FloatField(default=0, null=True, blank=True)
    audio_discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    audio_dic_price = models.FloatField(default=0, null=True, blank=True)
    audio_file = models.FileField(null=True, blank=True)

    pdf_price = models.FloatField(default=0, null=True, blank=True)
    pdf_discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    pdf_file = models.FileField(null=True, blank=True)
    pdf_dic_price = models.FloatField(default=0, null=True, blank=True)

    book_view = models.IntegerField(default=0, blank=True)

    image = models.ImageField(upload_to='images', blank=True, null=True)
    image1 = models.ImageField(upload_to='images', blank=True, null=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)

    def paper_disc(self):
        return self.paper_discount != 0

    def audio_disc(self):
        return self.audio_discount != 0

    def pdf_disc(self):
        return self.pdf_discount != 0

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class CommentModel(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'commets'


class AdminCommentModel(models.Model):
    com = models.ForeignKey(CommentModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Admin comment'
        verbose_name_plural = 'Admin commets'
