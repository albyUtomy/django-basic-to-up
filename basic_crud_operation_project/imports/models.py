# imports models from different apps

from app_school.models import School
from app_department.models import Department
from app_progress_student.models import Student_Progress
from app_teacher.models import Teacher


__all__ = ['School', 'Department', 'Student_Progress', 'Teacher']