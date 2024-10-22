from django.contrib import admin
from .models import Student_Progress, Teacher


# Register your models here.

class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'percentage', 'gained_mark','out_off' ,
                    'maths_mark', 'physics_mark', 'chemistry_mark', 'class_teacher_id')

admin.site.register(Student_Progress, StudentProgressAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name')

admin.site.register(Teacher,TeacherAdmin)