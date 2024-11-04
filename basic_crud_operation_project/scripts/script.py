from app_progress_student.models import *
# from utils.utils import teacher_analysis
from app_progress_student.models import Teacher
from app_department.models import Department
from app_school.models import School
import random


def depart_to_school():
    school_ids = School.objects.values_list('school_id', flat=True)
    print("School IDs:", school_ids)

    # for department_id , school_id in zip(department_ids, school_ids):
    #     print(department_id, school_id)
    for school_id in school_ids:
        department_ids = Department.objects.filter(school_id=school_id).values_list('department_id', flat=True)
        print(f"Departments linked to School ID {school_id}: {department_ids}")
        school = School.objects.get(school_id=school_id)
        school.department_id.set(department_ids)
        school.save()
        print(f"Assigned departments {department_ids} to school ID {school_id}")

def run():
    depart_to_school()