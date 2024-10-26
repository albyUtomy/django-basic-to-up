from rest_framework import serializers
from .models import Teacher

from app_department.models import Department
from app_department.serializers import DepartmentSerializer

class TeacherSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True, required=False)
    department_name = DepartmentSerializer(source='department_id',read_only=True)
    class Meta:
        model = Teacher
        fields = ['teacher_id','name', 'performance_rate', 'department_id', 'department_name']
