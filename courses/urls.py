from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (CoursesViewSet, ModulesViewSet, LessonsViewSet, 
                    LessonFilesViewSet, ArticleViewSet, CommentViewSet,
                    NotificationViewSet)


router = DefaultRouter()
router.register('courses', CoursesViewSet, basename='courses')
router.register('modules', ModulesViewSet, basename='modules')
router.register('lessons', LessonsViewSet, basename='lessons')
router.register('lesson_files', LessonFilesViewSet, basename='lesson_files')
router.register('articles', ArticleViewSet, basename='articles')
router.register('comments', CommentViewSet, basename='comments')
router.register('notificiations', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('', include(router.urls))
]