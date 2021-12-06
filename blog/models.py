from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=250)
    info = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
