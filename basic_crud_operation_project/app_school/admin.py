from django.contrib import admin
from .models import School

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_id','school_name','address','principle_name')

admin.site.register(School,SchoolAdmin)