from django.shortcuts import render

# imports from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# imports from models
from .models import Department
from app_teacher.models import Teacher
from .serializers import DepartmentSerializer


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
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({'error':'Departments data not found'}, status= status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request):
        try:
            department = Department.objects.all()
            if department.exists():
                department.delete()
                return Response({'message':'All department is successfully deleted'}, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({'message':'No records found to delete'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class Department_by_Id(APIView):
    def get(self, request, department_id):
        try:
            department = Department.objects.get(department_id=department_id)
            serializer = DepartmentSerializer(department)
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
        pass