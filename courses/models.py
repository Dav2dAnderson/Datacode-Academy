from django.db import models
from django.utils.text import slugify

from accounts.models import MyUser


class Article(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    

