from django.contrib import admin, messages
from .models import Department


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'hod_name','school_id', 'department_name')
    
    def save_model(self, request, obj, form, change):

        # Ensure that `hod_name` belongs to the same department before saving
        if obj.hod_name and obj.hod_name.department_id != obj:
            # Display warning to the user in the admin interface
            self.message_user(
                request, 
                f"The assigned HoD, {obj.hod_name.name}, does not belong to the {obj.department_name} department and was not saved as HoD.", 
                level=messages.WARNING
            )
            obj.hod_name = None  # Clear invalid HoD assignment to prevent save error

        super().save_model(request, obj, form, change)
admin.site.register(Department, DepartmentAdmin)