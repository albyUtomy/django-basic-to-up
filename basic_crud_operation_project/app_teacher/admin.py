from django.contrib import admin
from .models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name','is_active','performance_rate')
    list_filter = ('is_active',)

admin.site.register(Teacher, TeacherAdmin)