from django.contrib import admin, messages
from .models import Student_Progress


# Register your models here.

class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no','is_active','school_id','department_id','class_teacher_id' , 'percentage', 'gained_mark','out_off')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.warning_message:
            self.message_user(request, obj.warning_message, level=messages.WARNING)
        else:
            self.message_user(request, f"The student '{obj.name}' was created successfully.", level=messages.SUCCESS)
        

admin.site.register(Student_Progress, StudentProgressAdmin)

