
from django.db import models
from django.utils import timezone

class ActiveSchoolManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class InactiveSchoolManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)

class School(models.Model):
    school_id = models.IntegerField(primary_key=True, editable=False)
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    principal_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    department_id = models.ManyToManyField('app_department.Department', related_name='department_school')
    
    
    active_object = ActiveSchoolManager()
    inactive_object = InactiveSchoolManager()
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.school_id:
            last_school = School.objects.order_by('school_id').last()
            # self.school_id = last_school.school_id + 1 if 100 else 100
            if last_school:
                self.school_id = last_school.school_id + 1
            else:
                self.school_id = 100  # Starting ID for schools
        super(School, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.school_id} : {self.school_name}"

