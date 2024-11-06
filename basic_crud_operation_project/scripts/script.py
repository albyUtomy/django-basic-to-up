from app_progress_student.models import *
# from utils.utils import teacher_analysis
from app_progress_student.models import Teacher
from app_department.models import Department
from app_school.models import School
# from app_user.models import Custom_User
from app_user_authentication.models import Custom_User



import random
import string
from django.contrib.auth.hashers import make_password


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


def teacher_to_adduser():
    teachers = Teacher.objects.all()
    roles = ['teacher', 'hod', 'principal']

    for teacher in teachers:
        # Create username and random password
        username = f"{teacher.name.lower().replace(' ', '_')}_{teacher.teacher_id}"
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # Check if user with this username already exists
        if Custom_User.objects.filter(username=username).exists():
            print(f"Username '{username}' already exists")
            continue

        try:
            # Create new Custom_User
            user = Custom_User(
                username=username,
                last_login=timezone.now(),
                school=teacher.school_id,
                performance=teacher.performance_rate,
                role_as=random.choice(roles),
                employee_id =teacher.teacher_id
            )
            user.set_password(random_password)  # Set and hash password
            user.save()

            user.department.set(teacher.department_id.all())

            print(f"Created user: {user.username} with a generated password: {random_password}.")
            print("Hashed Password: ", user.password)

        except Exception as e:
            print(f"Error creating user {username}: {e}")


def run():
    # depart_to_school()
    teacher_to_adduser()
    # remove_superuser()