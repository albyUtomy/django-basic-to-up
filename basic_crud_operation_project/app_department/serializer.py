from rest_framework import serializers
from .models import Department

# model imports from apps
from app_progress_student.models import Teacher
from app_school.models import School


#serializer import from different apps
class DepartmentSerializer(serializers.ModelSerializer):
    hod_name = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), write_only=True, required=False)
    school_id = serializers.PrimaryKeyRelatedField(queryset = School.objects.all(), write_only=True,required=False)
    class Meta:
        model = Department
        fields = ['department_id','department_name','hod_name', 'school_id', 'created_at','updated_at']