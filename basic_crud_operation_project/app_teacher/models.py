from django.db import models
from django.utils import timezone

# from utils.utils import get_best_value
from django.db import transaction

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True)
    performance_rate = models.FloatField(blank=True, editable=False, null=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    department_id = models.ForeignKey('app_department.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='teachers_app_teacher')
    school_id = models.ForeignKey('app_school.School', on_delete=models.SET_NULL, null=True, blank=True, related_name='teachers_app_teacher')


    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)

            from utils.utils import assign_hod_name
            if self.department_id:
                # Pass the department instance to assign_hod_name
                assign_hod_name(self.department_id, self)
        


    def __str__(self):
        return f"{self.name} id : {self.teacher_id}"