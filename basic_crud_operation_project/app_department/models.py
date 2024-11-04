from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


# from utils.utils import get_best_value
# Create your models here.


class ActiveDepartmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class InactiveDepartmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)
    
class Department(models.Model):
    department_id = models.IntegerField(primary_key=True, editable=False)
    department_name = models.CharField(max_length=255)
    hod_name = models.OneToOneField('app_teacher.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='departments')
    # school_id = models.ForeignKey('app_school.School', on_delete=models.SET_NULL, null=True, blank=True, related_name='school_department')
    # created_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    active_object = ActiveDepartmentManager()
    inactive_object = InactiveDepartmentManager()
    objects = models.Manager()

    def save(self, *args, **kwargs):
        # Assign department_id if not already set
        if not self.department_id:
            last_department = Department.objects.order_by('department_id').last()
            self.department_id = last_department.department_id + 1 if last_department else 3000  # Starting ID for departments

        # Warning message initialization
        # self.warning_message = None

        # # Check if hod_name belongs to the same department and school
        if self.hod_name:
            # Validate that HoD belongs to the same department
            if self.hod_name.department_id != self:
                self.hod_name.department_id = None
                raise ValidationError(f"Warning: The assigned HoD, {self.hod_name.name}, must belong to the {self.department_name} department.")
                
            # Validate that HoD belongs to the same school
            elif self.hod_name.school_id != self.school_id:
                self.hod_name = None
                raise ValidationError(f"Warning: The assigned HoD, {self.hod_name.name}, must belong to the same school as the department.")

        # # Call the parent save method
        super(Department, self).save(*args, **kwargs)

        # # Handle the warning message after save
        # if self.warning_message:
        #     # You can choose to log this warning or raise an alert as needed
        #     print(self.warning_message)


    def __str__(self):
        return f"{self.department_id} : {self.department_name}"