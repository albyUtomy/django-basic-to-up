from app_progress_student.models import *
# from utils.utils import teacher_analysis
from app_progress_student.models import Teacher
from app_department.models import Department

def run():


# Check all employee_ids
    teachers = Teacher.objects.values_list('employee_id', flat=True)

    # Check departments with invalid hod_name
    departments_with_invalid_hod = Department.objects.exclude(hod_name__in=teachers)

    for department in departments_with_invalid_hod:
        print(department.department_name, department.hod_name)