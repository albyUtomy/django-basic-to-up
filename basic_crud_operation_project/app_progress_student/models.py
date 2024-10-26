from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.utils import get_percentage, teacher_analysis
from django.utils import timezone


from app_teacher.models import Teacher

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


    class_teacher_id = models.ForeignKey('app_teacher.Teacher', on_delete=models.SET_NULL, null=True)
    school_id = models.ForeignKey('app_school.School', on_delete=models.SET_NULL, null=True, blank=True, related_name='student')  # Total number of students
    department_id = models.ForeignKey('app_department.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='student')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        # Calculate percentage and gained marks
        self.gained_mark = sum([self.chemistry_mark or 0,
                                self.physics_mark or 0,
                                self.maths_mark or 0])
        
        if self.gained_mark > self.out_off:
            raise ValueError("Gained marks cannot exceed total possible marks.")

        self.percentage = get_percentage(self.chemistry_mark or 0, 
                                        self.physics_mark or 0, 
                                        self.maths_mark or 0, 
                                        total_possible=self.out_off)
        
        # Call super to save the Student_Progress instance
        super(Student_Progress, self).save(*args, **kwargs)

        if self.class_teacher_id:
            try:
                teacher = self.class_teacher_id
                student_data = Student_Progress.objects.filter(class_teacher_id=teacher)
                top_10 = student_data.order_by('-gained_mark')[:10]
                performance_data = teacher_analysis(student_data, top_10)
                
                teacher.performance_rate = performance_data.get('performance_rate_out_of_10', 0)
                teacher.save()
            except Exception as e:
                # Log or handle any errors that occur during saving
                print(f"Error updating teacher or department: {str(e)}")
    
    def __str__(self):
        return f"{self.name} ({self.roll_no})"
    



