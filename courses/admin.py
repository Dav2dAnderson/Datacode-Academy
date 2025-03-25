from django.contrib import admin

from .models import Article, Comment, Notification
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['to', 'sent_at']

