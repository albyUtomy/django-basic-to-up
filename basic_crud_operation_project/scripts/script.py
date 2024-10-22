from app_progress_student.models import *
from utils.utils import teacher_analysis

def run():
    teacher_id_lst = Teacher.objects.values_list('employee_id', flat=True)
    students = Student_Progress.objects.all()
    top_10_queryset = Student_Progress.objects.filter(gained_mark__isnull=False).order_by('-gained_mark')
    top_10_list = list(top_10_queryset)
    print(list(teacher_id_lst))

    for id in teacher_id_lst:
        students = Student_Progress.objects.filter(class_teacher_id = id)
        analysis = teacher_analysis(students, top_10_list)

        try:
            teacher = Teacher.objects.get(employee_id=id)
            teacher.performance_rate = analysis['performance_rate_out_of_10']
            teacher.save()
            print(f"Updated performance for Teacher ID {id}: {analysis['performance_rate_out_of_10']}")
        except Teacher.DoesNotExist:
            print(f"Teacher with ID {id} not found.")

    print("Analysis complete.")