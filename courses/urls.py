from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CoursesViewSet, ModulesViewSet, LessonsViewSet, LessonFilesViewSet


router = DefaultRouter()
router.register('courses', CoursesViewSet, basename='courses')
router.register('modules', ModulesViewSet, basename='modules')
router.register('lessons', LessonsViewSet, basename='lessons')
router.register('lesson_files', LessonFilesViewSet, basename='lesson_files')

urlpatterns = [
    path('', include(router.urls))
]