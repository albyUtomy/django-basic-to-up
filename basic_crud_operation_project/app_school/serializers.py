from rest_framework import serializers
from imports.models import School
from app_department.serializers import DepartmentSerializer


class SchoolSerializer(serializers.ModelSerializer):

    department_id = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = School
        fields = ['school_id','school_name','address','department_id','principal_name','is_active']

class ListSchoolSerializer(serializers.ModelSerializer):
    department_info = serializers.SerializerMethodField()
    class Meta:
        model = School
        fields = ['school_id','school_name','address','principal_name','department_info','is_active']

    def get_department_info(self, obj):
        # Get a flat list of department names
        return list(obj.department_id.values_list('department_id', 'department_name'))
    
class SchoolCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_id','school_name','principal_name','is_active']