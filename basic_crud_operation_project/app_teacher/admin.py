from django.contrib import admin
from .models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'performance_rate','department_id')

admin.site.register(Teacher, TeacherAdmin)