from rest_framework import serializers
from .models import Teacher

from app_department.models import Department
from app_department.serializers import DepartmentSerializer
from app_school.models import School

class TeacherSerializer(serializers.ModelSerializer):

    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), many=True, write_only=True, required=False
    )
    department_name = serializers.SlugRelatedField(
        slug_field='department_name', source='department_id', many=True, read_only=True
    )
    class Meta:
        model = Teacher
        fields = ['teacher_id','name', 'performance_rate', 'department_id','department_name','is_active']


    # def validate_department_id(self, value):
    #     # Ensure all provided department IDs exist
    #     if not value:  # Check if the list is empty
    #         raise serializers.ValidationError("At least one department ID must be provided.")
        
    #     invalid_ids = []
    #     for department_id in value:
    #         if not Department.objects.filter(department_id=department_id).exists():
    #             invalid_ids.append(department_id)
        
    #     if invalid_ids:
    #         raise serializers.ValidationError(f"Invalid department IDs: {', '.join(map(str, invalid_ids))}")

    #     return value

class TeacherDetailsSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True, required=False)
    class Meta:
        model = Teacher
        fields = ['teacher_id','name', 'performance_rate', 'department_id']

    