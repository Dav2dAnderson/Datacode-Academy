from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Nomi")
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    teach_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kurs")
    information = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="Tug'ilgan sana")
    courses = models.ManyToManyField(Course, related_name="courses", verbose_name="Kurslar")

    def __str__(self):
        return self.user.username
    




