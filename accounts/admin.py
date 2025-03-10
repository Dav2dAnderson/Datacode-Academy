from django.contrib import admin

from .models import MyUser, Courses, Modules, Lessons, LessonFile, CustomRole


@admin.register(CustomRole)
class RolesAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'email', 'role']


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'assistant', 'teacher', 'is_active']
    list_filter = ['name', 'is_active', 'teacher']
    search_fields = ['name', 'is_active', 'teacher', 'created_at']
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['name', ]
    search_fields = ['name', ]


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'created_at', 'updated_at', 'is_active']


@admin.register(LessonFile)
class LessonFileAdmin(admin.ModelAdmin):
    list_display = ['file', 'lesson']
    list_filter = ['file', 'lesson']
    search_fields = ['lesson']

