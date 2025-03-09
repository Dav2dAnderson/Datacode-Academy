from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions, filters

from accounts.models import Courses, Modules, LessonFile, Lessons
from accounts.permissions import IsTeacherOrAdminUser, IsStudent
from .serializers import (CourseListSerializer, CourseRetrieveSerializer, ModulesListSerializer, 
                          ModuleRetrieveSerializer, LessonsListSerializer, LessonRetrieveSerializer,
                          LessonFilesSerializer)
# Create your views here.


"""Course-lar uchun View"""
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    # serializer_class = CourseListSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
    permission_classes = [permissions.IsAuthenticated, IsTeacherOrAdminUser]
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

    def get_serializer_class(self):
        if self.action == 'list':
            return LessonsListSerializer
        return LessonRetrieveSerializer
    

"""Lesson file-lari uchun View"""
class LessonFilesViewSet(viewsets.ModelViewSet):
    queryset = LessonFile.objects.all()
    serializer_class = LessonFilesSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]