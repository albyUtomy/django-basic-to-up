from rest_framework import serializers
from imports.models import Department, Teacher, School

# from app_school.serializers import SchoolSerializer
# from app_teacher.serializers import TeacherSerializer


#serializer import from different apps
class DepartmentSerializer(serializers.ModelSerializer):
    hod_name = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), write_only=True, required=False)
    hod_details = serializers.StringRelatedField(source='hod_name', read_only=True)
    # school_id = serializers.PrimaryKeyRelatedField(queryset = School.objects.all(), write_only=True,required=False)
    # school_details = serializers.StringRelatedField(source = 'school_id',read_only=True)
    class Meta:
        model = Department
        fields = ['department_id','department_name','hod_name','hod_details','is_active']

    def validate(self, attribute):
        hod = attribute.get('hod_name')
        department =  self.instance or Department.objects.get(department_id = attribute.get('department_id'))

        if hod:
            if not hod.department_id.filter(department_id = department.department_id).exists():
                raise serializers.ValidationError(f"The assigned HoD, {hod.name}, must belong to the {department.department_name} department.")

            related_schools = department.department_school.all()
            if not any(school for school in related_schools if school.department_id.filter(pk=department.department_id).exists()):
                raise serializers.ValidationError(
                f"The assigned HoD, {hod.name}, must be associated with a school that includes the {department.department_name} department."
            )
        return attribute
# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ['department_id', 'name', 'school_id']  # Adjust fields as necessary
