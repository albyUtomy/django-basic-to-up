from django.contrib import admin
from .models import Department

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'hod_name','school_id', 'department_name')

admin.site.register(Department, DepartmentAdmin)