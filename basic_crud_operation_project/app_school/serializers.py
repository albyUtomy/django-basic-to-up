from rest_framework import serializers
from imports.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_id','school_name','address','principal_name']