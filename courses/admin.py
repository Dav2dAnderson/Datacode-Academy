from django.contrib import admin

from .models import Comment, Video
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'video', 'written_at']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'views']
    