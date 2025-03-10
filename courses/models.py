from django.db import models

from accounts.models import MyUser


class Article(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='article_images/')
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    