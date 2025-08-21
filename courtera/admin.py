from django.contrib import admin

from .models import User, Course, UserCourse
# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(UserCourse)
