from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

from django.utils import timezone
# Create your models here.

class Custom_User(AbstractUser):
    performance = models.FloatField(blank=True, editable=False, null=True)
    department = models.ManyToManyField('app_department.Department', blank=True, related_name='department_connect')
    school = models.ForeignKey('app_school.School', on_delete=models.SET_NULL, null=True, blank=True, related_name='school_connect')
    is_active = models.BooleanField(default=True)    
    role_as = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(Group,related_name="group_so", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="permission_so", blank=True)
    employee_id = models.IntegerField(blank=True, null=True)

    
    def __str__(self):
        return f"{self.username} : {self.pk}"