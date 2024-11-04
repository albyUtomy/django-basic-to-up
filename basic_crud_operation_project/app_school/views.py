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


from django.shortcuts import get_object_or_404


from .serializers import SchoolSerializer,ListSchoolSerializer,SchoolCommonSerializer
from app_department.serializers import DepartmentSerializer
from app_teacher.serializers import TeacherDetailsSerializer
from app_progress_student.serializers import StudentDetail

import logging
# logger = logging.getLogger(__name__)

class SchoolCrud(APIView):
    queryset = School.objects.all()

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            school = serializer.save()
            department_ids = request.data.get('department_id', [])

            for department_id in department_ids:
                try:
                    department = Department.active_object.get(department_id=department_id)
                    school.department_id.add(department)
                except Department.DoesNotExist:
                    return Response({
                        "error": f"Department with ID {department_id} not found or inactive"
                        }, status=status.HTTP_404_NOT_FOUND)
            return Response(SchoolSerializer(school).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        school = School.objects.all()
        serializer = SchoolCommonSerializer(school, many=True)
        return Response(serializer.data)
    

class SchoolCrudById(APIView):
    queryset = School.objects.all()

    def get(self, request, school_id=None):
        if school_id:
            try:
                school = School.active_object.get(school_id=school_id)
                department_names = school.department_id.values_list('department_name', flat=True)
                school_data = ListSchoolSerializer(school).data
                school_data['department_id'] = list(department_names)
                return Response(school_data)
            except School.DoesNotExist:
                return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            schools = School.objects.all()
            serializer = ListSchoolSerializer(schools, many=True)
            return Response(serializer.data)
    

    def put(self, request, school_id=None):
        try:
            school = School.objects.get(school_id=school_id)
        except School.DoesNotExist:
            return Response({'error': "School not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SchoolSerializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            updated_school = serializer.save()
            department_ids = request.data.get('department_id')
            
            if department_ids:
                try:
                    departments = Department.active_object.filter(department_id__in=department_ids)
                    updated_school.department_id.set(departments)
                except Department.DoesNotExist:
                    return Response({"error": "Check if the department ID exists"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(SchoolSerializer(updated_school).data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class Filtration(APIView):
    def get(self, request, school_id):
        try:
            if '/departments/' in request.path:
                school = School.objects.get(school_id=school_id)
                departments = school.department_id.all()  # Many-to-many relationship
                serializer = DepartmentSerializer(departments, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            elif '/teachers/' in request.path:
                teachers = Teacher.active_objects.filter(school_id=school_id).values_list('name','department_id__department_name')
                teachers_obj = [
                    {
                        'teacher_name': teacher[0],
                        'department_name': teacher[1]
                    } for teacher in teachers
]
                if not teachers.exists():
                    return Response({'message':'Teacher not found'},status=status.HTTP_404_NOT_FOUND)
                return Response({'Teachers':teachers_obj}, status=status.HTTP_200_OK)
            
            elif '/students/' in request.path:
                students = Student_Progress.objects.filter(school_id=school_id, is_active=True).values_list('name', 'department_id__department_name', 'class_teacher_id_id__name')
                students_obj = [
                    {
                    'student_name':student[0],
                    'department_name':student[1],
                    'teacher_name':student[2]
                    }for student in students
                ]
                if not students.exists():
                    return Response({'message':'Students not found'},status=status.HTTP_404_NOT_FOUND)
                # st_serializers = StudentDetail(students, many=True)
                return Response({'Students':students_obj}, status=status.HTTP_200_OK)
            
            return Response({'message': 'Invalid request path'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class MakeInActive(APIView):
    def get(self,request, school_id):
        school = get_object_or_404(School, school_id=school_id, is_active=True)
        school.is_active = False
        school.save()

        departments = Department.objects.filter(school_id=school_id).update(school_id=None)
        teachers = Teacher.active_objects.filter(school_id=school_id).update(school_id=None)
        students = Student_Progress.objects.filter(school_id=school_id).update(school_id=None)


        # Prepare the names for the response

        # Create a response message
        response_message = {
            'message': f'School {school.school_name}, id: {school_id} has been inactivated'
        }
        return Response(response_message, status=status.HTTP_200_OK)
    
class ActiveOrInActive(APIView):
    def get(self, request, active_or_not):
        try:
            if active_or_not == 'is_active' in request.path:
                school = School.active_object.all()
                serializer = SchoolCommonSerializer(school, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            if  active_or_not == 'is_inactive' in request.path:
                school = School.inactive_object.all()
                serializer = SchoolCommonSerializer(school, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)