from rest_framework import serializers
from imports.models import Department, Teacher, School

from app_school.serializers import SchoolSerializer
# from app_teacher.serializers import TeacherSerializer


#serializer import from different apps
class DepartmentSerializer(serializers.ModelSerializer):
    hod_name = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), write_only=True, required=False)
    hod_details = serializers.StringRelatedField(source='hod_name', read_only=True)
    school_id = serializers.PrimaryKeyRelatedField(queryset = School.objects.all(), write_only=True,required=False)
    school_details = serializers.StringRelatedField(source = 'school_id',read_only=True)
    class Meta:
        model = Department
        fields = ['department_id','department_name','hod_name','hod_details', 'school_id','school_details']