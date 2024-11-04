from django.contrib import admin, messages
from .models import Department


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name','is_active', 'hod_name')
    list_filter = ('is_active',)
    
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)

    #     if obj.warning_message:
    #         self.message_user(request, obj.warning_message, level=messages.WARNING)
    #     else:
    #         self.message_user(request, f"The department '{obj.department_name}' was changed successfully.", level=messages.SUCCESS)
        
admin.site.register(Department, DepartmentAdmin)