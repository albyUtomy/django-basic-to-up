from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name', 'employee_id','performance_rate']
