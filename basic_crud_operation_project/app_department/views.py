from django.shortcuts import render

# imports from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# imports from models
from .models import Department
from app_teacher.models import Teacher
from app_progress_student.models import Student_Progress
from .serializers import DepartmentSerializer
from app_teacher.serializers import TeacherSerializer
from app_progress_student.serializers import StudentProcessSerializer


class DepartmentCrud(APIView):
    def post(self, request):
        try:
            serializers = DepartmentSerializer(data=request.data, many=True)
            if serializers.is_valid():
                serializers.save()
                return Response({'message':'Record created successfully','data':serializers.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    def get(self, request):
        try:
            departments = Department.objects.filter(is_active=True)
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({'error':'Departments data not found'}, status= status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class Department_by_Id(APIView):
    def get(self, request, department_id):
        try:
            department = Department.objects.filter(department_id=department_id, is_active=True)
            serializer = DepartmentSerializer(department, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({'message':'Id not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, department_id):
        try:
            department = Department.objects.get(department_id=department_id)
            serializer = DepartmentSerializer(department,data=request.data, partial=True)

            hod_name_id = request.data.get('hod_name')
            if hod_name_id:
                    hod_teacher = Teacher.objects.filter(teacher_id = hod_name_id, department_id=department_id).first()
                    if not hod_teacher:
                        valid_teachers = Teacher.objects.filter(department_id=department_id).values('teacher_id', 'name')
                        return Response({'message': f'The assigned HoD (Teacher ID {hod_name_id}) does not belong to "{department.department_name}" department.','valid_teachers': list(valid_teachers)}, status=status.HTTP_400_BAD_REQUEST)
                

            if serializer.is_valid():
                serializer.save()
                return Response({'message':f'{department.department_name} : {department.department_id} successfully updated'}, status=status.HTTP_202_ACCEPTED)
            return Response({'message':'Invalid data', 'details':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Department.DoesNotExist:
            return Response({'message':'Id not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    def delete(self, request, department_id):
        try:
            department = Department.objects.get(department_id=department_id)
            department_name, departmentID = department.department_name, department.department_id
            department.delete()
            return Response({'message':f'{department_name} : {departmentID} got deleted'})
        except Department.DoesNotExist:
            return Response({'message':'Department Id not Found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DepartmentSort(APIView):
    def get(self, request, department_id):
        """
        /department_filter
        try:
            teachers = Teacher.objects.filter(department_id = department_id)
            students = Student_Progress.objects.filter(department_id=department_id)

            missing_messages = []
            if not teachers.exists():
                missing_messages.append('No teachers found for this department')
            if not students.exists():
                missing_messages.append('No students found for this department')

            # If either teachers or students are missing, return the combined message
            if missing_messages:
                return Response({'message': ' and '.join(missing_messages)}, status=status.HTTP_404_NOT_FOUND)

            t_serializers = TeacherSerializer(teachers, many=True)
            s_serializers = StudentProcessSerializer(students, many=True)
            return Response({'Teachers':t_serializers.data, 'Students':s_serializers.data}, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist or Student_Progress.DoesNotExist:
            return Response({'message':'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    """

        try:
            # Check the requested path to determine if it's a student or teacher request
            if '/department_teacher' in request.path:
                teachers = Teacher.objects.filter(department_id=department_id).order_by('name')  # Sort by name
                if not teachers.exists():
                    return Response({'message': 'No teachers found for this department'}, status=status.HTTP_404_NOT_FOUND)
                t_serializers = TeacherSerializer(teachers, many=True)
                return Response({"Teacher's List": t_serializers.data}, status=status.HTTP_200_OK)

            elif '/department_student' in request.path:
                students = Student_Progress.objects.filter(department_id=department_id).order_by('-marks')  # Sort by marks
                if not students.exists():
                    return Response({'message': 'No students found for this department'}, status=status.HTTP_404_NOT_FOUND)
                s_serializers = StudentProcessSerializer(students, many=True)
                return Response({'Students': s_serializers.data}, status=status.HTTP_200_OK)
            
            # If neither student nor teacher is specified, return an error
            return Response({'message': 'Invalid request path'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'message': 'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)