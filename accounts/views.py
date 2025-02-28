from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Teacher, Student, Course
from .serializers import StudentSerializer
# Create your views here.


class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser, ]


