from django.shortcuts import render

# imports from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# imports from models
from .models import Department
from .serializer import DepartmentSerializer


class DepartmentCrud(APIView):
    def get(self, request):
        try:
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data)
        except Department.DoesNotExist:
            return Response({'error':'Departments data not found'}, status= status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)