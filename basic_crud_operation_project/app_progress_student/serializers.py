from rest_framework import serializers

# importing required serializers and models from imports
# from imports.models import  Teacher, Department, School
# from .models import Student_Progress


from app_department.models import Department
from app_teacher.models import Teacher
from app_school.models import School
from app_progress_student.models import Student_Progress

# from app_teacher.serializers import TeacherSerializer
# from app_school.serializers import SchoolSerializer
# from app_department.serializers import DepartmentSerializer

class StudentProcessSerializer(serializers.ModelSerializer):
    class_teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    # class_teacher = serializers.SerializerMethodField()
    # class_teacher = serializers.StringRelatedField(source='class_teacher_id', read_only=True)

    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    # department_details = serializers.StringRelatedField(source='department_id', read_only=True)

    school_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    # school_details = serializers.StringRelatedField(source='school_id', read_only=True)

    class Meta:
        model = Student_Progress
        fields = [
                    'roll_no',
                    'name',
                    'percentage',
                    'gained_mark',
                    'out_off',
                    'class_teacher_id',
                    # 'class_teacher',
                    'school_id',
                    # 'school_details',
                    'department_id',
                    # 'department_details',
                    'is_active'
                    
                ]
        
        read_only_fields = ['roll_no','percentage', 'gained_mark', 'out_off']

    # def get_class_teacher(self, obj):
    #     from imports.serializers import TeacherSerializer
    #     return TeacherSerializer(obj.class_teacher_id).data


class StudentDetail(serializers.ModelSerializer):

    class_teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), write_only=True, required=False)
    # class_teacher = serializers.SerializerMethodField()
    class_teacher = serializers.StringRelatedField(source='class_teacher_id', read_only=True)

    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True, required=False)
    department_details = serializers.StringRelatedField(source='department_id', read_only=True)

    class Meta:
        model = Student_Progress
        fields = [
                    'roll_no',
                    'name',
                    'class_teacher_id',
                    'class_teacher',
                    'department_id',
                    'department_details',
                ]
        
        read_only_fields = ['roll_no']

    
    

"""
Method 1
class ChemistryMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Progress
        fields = ['name','roll_no', 'chemistry_mark']

class PhysicsMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Progress
        fields = ['name','roll_no', 'physics_mark']


class MathsMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Progress
        fields = ['name','roll_no', 'maths_mark']

        
"""


"""
Method 2 create single serializer for all and use for loop to iterate over it to fetch specific data
"""




class CombinedMarksSerializer(serializers.ModelSerializer):
    chemistry_mark = serializers.FloatField(read_only=True)
    physics_mark = serializers.FloatField(read_only=True)
    maths_mark = serializers.FloatField(read_only=True)
    class Meta:
        model = Student_Progress
        fields = ['name', 'roll_no', 'chemistry_mark', 'physics_mark', 'maths_mark', 'gained_mark','percentage']


