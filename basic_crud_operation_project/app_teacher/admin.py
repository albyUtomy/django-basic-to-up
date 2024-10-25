from django.contrib import admin
from .models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'performance_rate')

admin.site.register(Teacher, TeacherAdmin)