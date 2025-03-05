from django.contrib import admin

from .models import *

admin.site.register(MyUser)
admin.site.register(Courses)
admin.site.register(Modules)
admin.site.register(Lessons)
admin.site.register(LessonFile)
