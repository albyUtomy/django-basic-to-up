from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.
from .models import School
from app_department.models import Department
from app_teacher.models import Teacher
from app_progress_student.models import Student_Progress


from .serializers import SchoolSerializer
from app_department.serializers import DepartmentSerializer
from app_teacher.serializers import TeacherDetailsSerializer
from app_progress_student.serializers import StudentDetail

import logging
# logger = logging.getLogger(__name__)

class SchoolCrud(APIView):
    def post(self, request):
        try:
            serializer = SchoolSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':serializer.data},status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # logger.error(f"Error creating school: {e}" )
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            
    def get(self, request):
        try:
            school = School.objects.all()
            serializer = SchoolSerializer(school, many=True)

            return Response(serializer.data,status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({'error':'Schools data is not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):        
        try:
            school = School.objects.all()
            if school.exists():
                school.delete()
                return Response({'message':'All school has been deleted'}, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({'message':'No records found to delete'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


        

class SchoolUpdateRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, update, delete by id
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'school_id'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True 
        return super().update(request, *args, **kwargs)
    

class Filtration(APIView):
    def get(self, request, school_id):
        try:
            if '/departments/' in request.path:
                department = Department.objects.filter(school_id=school_id)
                if not department.exists():
                    return Response({'message':'Department not found'},status=status.HTTP_404_NOT_FOUND)
                d_serializers = DepartmentSerializer(department, many=True)
                return Response({'Departments':d_serializers.data}, status=status.HTTP_200_OK)
            
            elif 'school/teachers' in request.path:
                teachers = Teacher.objects.filter(school_id=school_id)
                if not teachers.exists():
                    return Response({'message':'Teacher not found'},status=status.HTTP_404_NOT_FOUND)
                t_serializers = TeacherDetailsSerializer(teachers, many=True)
                return Response({'Teachers':t_serializers.data}, status=status.HTTP_200_OK)
            
            elif '/students/' in request.path:
                students = Student_Progress.objects.filter(school_id=school_id)
                if not students.exists():
                    return Response({'message':'Students not found'},status=status.HTTP_404_NOT_FOUND)
                st_serializers = StudentDetail(students, many=True)
                return Response({'Students':st_serializers.data}, status=status.HTTP_200_OK)
            
            return Response({'message': 'Invalid request path'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)