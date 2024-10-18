from django.contrib import admin
from .models import Student_Progress


# Register your models here.

class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'class_teacher', 'percentage', 'gained_mark','out_off' ,
                    'maths_mark', 'physics_mark', 'chemistry_mark')

admin.site.register(Student_Progress, StudentProgressAdmin)