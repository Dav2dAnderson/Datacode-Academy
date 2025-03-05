from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import phone_validator


class MyUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('assistant', 'Assistant'),
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=13, blank=True, null=True, validators=[phone_validator])
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = "MyUser "
        verbose_name_plural = "MyUsers"


class Courses(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    assistant = models.ForeignKey(MyUser,
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True,
                                  related_name='assistant_courses',
                                  limit_choices_to={'role': 'assistant'})

    teacher = models.ForeignKey(MyUser,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='teacher_courses',
                                limit_choices_to={'role': 'teacher'})

    students = models.ManyToManyField(MyUser,
                                      related_name='student_courses',
                                      limit_choices_to={'role': 'student'},
                                      blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Course "
        verbose_name_plural = "Courses"


class Modules(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="modules")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Module "
        verbose_name_plural = "Modules"


class Lessons(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    module = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Lesson "
        verbose_name_plural = "Lessons"


class LessonFile(models.Model):
    file = models.FileField(upload_to='lessons/')
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='lesson_files')

    def __str__(self):
        return self.lesson.title

    class Meta:
        verbose_name = "Lesson File "
        verbose_name_plural = "Lesson Files"



    




