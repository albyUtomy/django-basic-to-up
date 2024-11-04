from rest_framework import serializers
from .models import Teacher

from app_department.models import Department
from app_department.serializers import DepartmentSerializer
from app_school.models import School

class TeacherSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True, required=False)
    department_name = serializers.StringRelatedField(source='department_id',read_only=True)
    class Meta:
        model = Teacher
        fields = ['teacher_id','name', 'performance_rate', 'department_id', 'department_name','is_active']


    def validate(self, attributes):
            department_ids = attributes.get('department_id', [])
            if not department_ids:
                 raise serializers.ValidationError("At least one department ID must be provided.")
            
            active_departments = []
            for department_id in active_departments:
                try:
                    department = Department.objects.get(department_id=department_id, is_active=True)
                    active_departments.append(department)
                except Department.DoesNotExist:
                    raise serializers.ValidationError(f"Department with ID {department_id} does not exist or is not active.")


class TeacherDetailsSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True, required=False)
    department_name = serializers.StringRelatedField(source='department_id', read_only=True)
    class Meta:
        model = Teacher
        fields = ['teacher_id','name', 'performance_rate', 'department_id', 'department_name']

    