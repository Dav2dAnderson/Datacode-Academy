from django.contrib import admin

from .models import Teacher, Student, Course
# Register your models here.


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'teach_course', 'birth_date']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', ]


