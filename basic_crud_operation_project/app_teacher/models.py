from django.db import models
from django.utils import timezone

# from utils.utils import get_best_value
# from django.db import transaction

# Create your models here.

class ActiveTeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class InactiveTeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)

class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True)
    performance_rate = models.FloatField(blank=True, editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    department_id = models.ManyToManyField('app_department.Department', blank=True, related_name='teachers_app_teacher')
    school_id = models.ForeignKey('app_school.School', on_delete=models.SET_NULL, null=True, blank=True, related_name='teachers_app_teacher')
    is_active = models.BooleanField(default=True)


    active_objects = ActiveTeacherManager()
    inactive_objects = InactiveTeacherManager()
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.teacher_id:
            last_teacher = Teacher.objects.order_by('teacher_id').last()
            if last_teacher:
                self.teacher_id = last_teacher.teacher_id + 1
            else:
                self.teacher_id = 2000
            
        super(Teacher, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.teacher_id} : {self.name}"