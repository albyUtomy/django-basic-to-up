from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.utils import get_percentage, teacher_analysis

# Create your models here.
class Student_Progress(models.Model):
    roll_no = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    chemistry_mark = models.FloatField(blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    physics_mark = models.FloatField(blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    maths_mark = models.FloatField(blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    out_off = models.IntegerField(blank=True, null=True,default=300, editable=False)
    gained_mark = models.FloatField(blank=True, null=True, editable=False)
    percentage = models.FloatField(editable=False, blank=True, null=True)
    class_teacher_id = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.percentage =  get_percentage(self.chemistry_mark or 0, 
                                          self.physics_mark or 0, 
                                          self.maths_mark or 0, 
                                          total_possible=300)
        
        self.gained_mark = sum([self.chemistry_mark or 0,
                                self.physics_mark or 0,
                                self.maths_mark or 0])
        
        super(Student_Progress, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} ({self.roll_no})"
    

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    employee_id = models.IntegerField(primary_key=True, editable=False)
    performance_rate = models.FloatField(blank=True, editable=False, null=True,)

    def __str__(self):
        return f"{self.name} id : {self.employee_id}"
    
    def save(self, *args, **kwargs):
        student_data = Student_Progress.objects.filter(class_teacher_id=self.employee_id)
        top_10 = Student_Progress.objects.order_by('-gained_mark')[:10]
        performance_data = teacher_analysis(self, student_data, top_10)
        self.performance_rate = performance_data['performance_rate_out_of_10']        
        super(Teacher, self).save(*args, **kwargs)
