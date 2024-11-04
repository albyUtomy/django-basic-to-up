import random
from django.core.management.base import BaseCommand
from app_teacher.models import Teacher
from app_department.models import Department
from app_school.models import School
from app_progress_student.models import Student_Progress

class Command(BaseCommand):
    help = 'Create sample data for students, schools, departments, and teachers'

    def handle(self, *args, **kwargs):
        # Create schools
        schools = []
        for i in range(5):
            school, created = School.objects.get_or_create(school_id=100 + i, school_name=f'School {100 + i}')
            schools.append(school)

        # Create departments and teachers
        departments = []
        teachers = []
        existing_teacher_ids = set(Teacher.objects.values_list('teacher_id', flat=True))  # Get existing teacher IDs

        for school in schools:
            for j in range(4):  # 4 departments per school
                department, created = Department.objects.get_or_create(
                    department_id=3000 + len(departments), 
                    department_name=f'Department {3000 + len(departments)}', 
                    school_id=school
                )
                departments.append(department)

                for k in range(9):  # 9 teachers per department
                    teacher_id = max(existing_teacher_ids, default=2000) + len(teachers) + 1  # Increment based on existing IDs
                    existing_teacher_ids.add(teacher_id)  # Add to set to track existing IDs

                    teacher, created = Teacher.objects.get_or_create(
                        teacher_id=teacher_id,
                        defaults={
                            'name': f'Teacher {teacher_id}', 
                            'department_id': department, 
                            'school_id': school
                        }
                    )
                    teachers.append(teacher)

        # Create students
        for i in range(60):
            school = random.choice(schools)
            department = random.choice(departments)
            class_teacher = random.choice([teacher for teacher in teachers if teacher.department_id == department])

            # Generate random marks
            chemistry_mark = random.randint(0, 100)
            physics_mark = random.randint(0, 100)
            maths_mark = random.randint(0, 100)

            # Randomly assign 12 students as failed
            if i < 12:
                chemistry_mark = random.randint(0, 49)  # Marks to ensure failure
                physics_mark = random.randint(0, 49)
                maths_mark = random.randint(0, 49)

            Student_Progress.objects.create(
                roll_no=None,  # Auto-incremented based on your model
                name=f'Student {i + 1}',
                chemistry_mark=chemistry_mark,
                physics_mark=physics_mark,
                maths_mark=maths_mark,
                class_teacher_id=class_teacher,
                school_id=school,
                department_id=department
            )

        self.stdout.write(self.style.SUCCESS('Successfully created sample data for students, schools, departments, and teachers'))
