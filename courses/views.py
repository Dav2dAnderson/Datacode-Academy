from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import Courses, Modules, LessonFile, Lessons
from accounts.permissions import IsTeacherOrAdminUser, IsStudent, IsAdminOrReadOnly
from .serializers import (CourseListSerializer, CourseRetrieveSerializer, ModulesListSerializer,
                          ModuleRetrieveSerializer, LessonsListSerializer, LessonRetrieveSerializer,
                          LessonFilesSerializer, ArticleSerializer, CommentSerializer, 
                          NotificationListSerializer, NotificationRetrieveSerializer)

from .models import Article, Comment, Notification

"""Course-lar uchun View"""
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseListSerializer
    lookup_field = "slug"   
    permission_classes = [IsAdminOrReadOnly | permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['created_at']
    search_fields = ['name', ]
    ordering_fields = ['created_at', ]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Courses.objects.all()
        return Courses.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseRetrieveSerializer


"""Module-lar uchun View"""
class ModulesViewSet(viewsets.ModelViewSet):
    queryset = Modules.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTeacherOrAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['course', 'created_at']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ModulesListSerializer
        return ModuleRetrieveSerializer


"""Lesson-lar uchun ViewSet"""
class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    lookup_field = 'slug'
    serializer_class = LessonsListSerializer
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['module']
    search_fields = ['title']
    ordering_fields = ['title', 'created_at', 'updated_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return LessonsListSerializer
        return LessonRetrieveSerializer


"""Lesson file-lari uchun View"""
class LessonFilesViewSet(viewsets.ModelViewSet):
    queryset = LessonFile.objects.all()
    serializer_class = LessonFilesSerializer
    permission_classes = [IsTeacherOrAdminUser]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lesson']



"""Article va Comment-lar uchun View"""
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']


"""Koment-lar uchun ViewSet"""
class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()
        else:
            self.permission_denied(self.request, message="Siz faqatgina o'z koment-laringizni tahrirlay olasiz.")

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()
        else:
            self.permission_denied(self.request, message="Siz faqat o'z koment-laringizni o'chira olasiz.")


"""Notification-lar uchun ViewSet"""
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Notification.objects.all()
        return user.notifications.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return NotificationListSerializer
        else:
            return NotificationRetrieveSerializer