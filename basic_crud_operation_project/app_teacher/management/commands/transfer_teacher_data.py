from django.core.management.base import BaseCommand
from app_progress_student.models import Teacher as OldTeacher  # Adjust this import based on your old model's actual name
from app_teacher.models import Teacher

class Command(BaseCommand):
    help = 'Transfer teacher data from app_progress_student to app_teacher'

    def handle(self, *args, **kwargs):
        # Get all old teachers
        old_teachers = OldTeacher.objects.all()

        for old_teacher in old_teachers:
            # Create a new teacher in the app_teacher app
            new_teacher = Teacher(
                employee_id=old_teacher.employee_id,  # Use the old employee_id
                name=old_teacher.name,
                performance_rate=old_teacher.performance_rate,
                department_id=old_teacher.department_id,  # Ensure this FK reference is valid
                school_id=old_teacher.school_id,        # Ensure this FK reference is valid
            )
            new_teacher.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully transferred teacher {new_teacher.name} with employee_id {new_teacher.employee_id}'))
