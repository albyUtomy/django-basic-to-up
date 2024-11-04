from django.db import models, transaction
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.utils import get_percentage, teacher_analysis
from django.utils import timezone


from app_teacher.models import Teacher


class ActiveStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class InactiveStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)
# Create your models here.
class Student_Progress(models.Model):
    roll_no = models.IntegerField(primary_key=True, editable=False)
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
    is_active = models.BooleanField(default=True)

    active_object = ActiveStudentManager()
    inactive_object = InactiveStudentManager()
    objects = models.Manager()


    warning_message = None

    def save(self, *args, **kwargs):
        # Assign roll number if not already set
        if not self.roll_no:
            last_student = Student_Progress.objects.order_by('roll_no').last()
            self.roll_no = last_student.roll_no + 1 if last_student else 1000  # Starting ID for students

        # Calculate gained marks
        self.gained_mark = sum([self.chemistry_mark or 0,
                                self.physics_mark or 0,
                                self.maths_mark or 0])
        
        # Validate gained marks
        if self.gained_mark > self.out_off:
            raise ValueError("Gained marks cannot exceed total possible marks.")

        # Calculate percentage
        self.percentage = get_percentage(self.chemistry_mark or 0, 
                                        self.physics_mark or 0, 
                                        self.maths_mark or 0, 
                                        total_possible=self.out_off)

        # Call the parent save method

         # Update teacher performance if class_teacher_id is set
        if self.class_teacher_id:
            try:
                with transaction.atomic():  # Transaction block for performance update
                    student_data = Student_Progress.objects.filter(class_teacher_id=self.class_teacher_id)
                    top_10 = student_data.order_by('-gained_mark')[:10]

                    # Update teacher's performance rate
                    from utils.utils import teacher_analysis
                    performance_data = teacher_analysis(student_data, top_10)
                    self.class_teacher_id.performance_rate = performance_data.get('performance_rate_out_of_10', 0)
                    self.class_teacher_id.save()
            except Exception as e:
                print(f"Error updating teacher's performance: {str(e)}")

        super(Student_Progress, self).save(*args, **kwargs)
            
        # Call super to save the Student_Progress instance

        # if self.class_teacher_id:
        #     teacher = self.class_teacher_id
            
        #     # Ensure the teacher's department is linked to the same school as the student
        #     if teacher and teacher.department_id and teacher.department_id.school_id != self.school_id:
        #         self.warning_message = "The teacher's department must belong to the same school as the student."
        #         self.department_id = None
        #         self.class_teacher_id = None
        #     else:
        #         self.warning_message = None  
        # super(Student_Progress, self).save(*args, **kwargs)
        

        # if self.class_teacher_id:
        #     try:
        #         teacher = self.class_teacher_id
        #         student_data = Student_Progress.objects.filter(class_teacher_id=teacher)
        #         top_10 = student_data.order_by('-gained_mark')[:10]
        #         performance_data = teacher_analysis(student_data, top_10)
                
        #         teacher.performance_rate = performance_data.get('performance_rate_out_of_10', 0)
        #         teacher.save()
        #     except Exception as e:
        #         # Log or handle any errors that occur during saving
        #         print(f"Error updating teacher or department: {str(e)}")
            
    
    def __str__(self):
        return f"{self.roll_no} : {self.name}"
    



