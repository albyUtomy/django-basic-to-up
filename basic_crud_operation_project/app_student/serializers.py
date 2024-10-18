from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):  # ModelSerializer (singular)
    class Meta:
        model = Students  # Ensure this matches your model's name
        fields = "__all__"  # This will include all fields of the model
