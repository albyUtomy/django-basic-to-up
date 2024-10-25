from django.db import models
from django.utils import timezone

# Create your models here.

class Teacher(models.Model):
    employee_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True)
    performance_rate = models.FloatField(blank=True, editable=False, null=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    department_id = models.ForeignKey('app_department.Department', on_delete=models.PROTECT, null=True, blank=True, related_name='teachers_app_teacher')
    school_id = models.ForeignKey('app_school.School', on_delete=models.PROTECT, null=True, blank=True, related_name='teachers_app_teacher')


    def __str__(self):
        return f"{self.name} id : {self.employee_id}"