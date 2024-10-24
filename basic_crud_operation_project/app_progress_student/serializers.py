from rest_framework import serializers
from .models import Student_Progress, Teacher



class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name', 'employee_id','performance_rate']



class StudentProcessSerializer(serializers.ModelSerializer):
    class_teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), write_only=True, required=False)
    class_teacher = TeacherSerializer(source='class_teacher_id',read_only=True)

    class Meta:
        model = Student_Progress
        fields = [
                    'roll_no',
                    'name',
                    'percentage',
                    'gained_mark',
                    'out_off',
                    'chemistry_mark',
                    'physics_mark',
                    'maths_mark',
                    'class_teacher_id',
                    'class_teacher',
                    'created_at',
                    'updated_at'
                ]
        
        read_only_fields = ['roll_no','percentage', 'gained_mark', 'out_off']

    def create(self, validated_data):
        return Student_Progress.objects.create(**validated_data)
    

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


