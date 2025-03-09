from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

from .validators import phone_validator, validate_file_extension


class CustomRole(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('assistant', 'Assistant'),
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]

    name = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    role = models.ForeignKey(CustomRole, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=13, blank=True, null=True, validators=[phone_validator])
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = "MyUser "
        verbose_name_plural = "MyUsers"


class Courses(models.Model):
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)    
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    assistant = models.ForeignKey(MyUser,
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True,
                                  related_name='assistant_courses',
                                  )

    teacher = models.ForeignKey(MyUser,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='teacher_courses',
                                )

    students = models.ManyToManyField(MyUser,
                                      related_name='student_courses',
                                      blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = "Course "
        verbose_name_plural = "Courses"


class Modules(models.Model):
    file = models.FileField(upload_to='module_images/', validators=[validate_file_extension], null=True, blank=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="modules")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = "Module "
        verbose_name_plural = "Modules"


class Lessons(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    module = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name = "Lesson "
        verbose_name_plural = "Lessons"


class LessonFile(models.Model):
    file = models.FileField(upload_to='lessons/', validators=[validate_file_extension])
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='lesson_files')

    def __str__(self):
        return self.lesson.title

    class Meta:
        verbose_name = "Lesson File "
        verbose_name_plural = "Lesson Files"



    




