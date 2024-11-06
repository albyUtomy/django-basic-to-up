# serializers.py
from rest_framework import serializers
from .models import Custom_User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ['username', 'password', 'email', 'performance', 'role_as', 'department', 'school', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},  # Make password write-only
            'is_active': {'default': True},  # Set default for is_active
        }

    def create(self, validated_data):
        user = Custom_User(
            username=validated_data['username'],
            email=validated_data.get('email'),
            performance=validated_data.get('performance'),
            role_as=validated_data.get('role_as'),
            is_active=validated_data.get('is_active', True)
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)