from django.db import models
from django.utils import timezone
# Create your models here.

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
        
    hod_name = models.ForeignKey('app_teacher.Teacher', on_delete=models.PROTECT, null=True, blank=True, related_name='departments')
    school_id = models.ForeignKey('app_school.School', on_delete=models.PROTECT, null=True, blank=True, related_name='school_department')
    
    # created_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name