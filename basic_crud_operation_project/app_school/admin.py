from django.contrib import admin
from .models import School

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_id','school_name','is_active','principal_name','address')

admin.site.register(School,SchoolAdmin)