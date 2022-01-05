from django.db import models


class PostModel(models.Model):
    image = models.ImageField(upload_to='image')
    image1 = models.ImageField(upload_to='image')
    image2 = models.ImageField(upload_to='image')
    title = models.CharField(max_length=250)
    info = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

