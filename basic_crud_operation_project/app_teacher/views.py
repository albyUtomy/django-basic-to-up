from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F

from .models import Teacher
from app_department.models import Department
from app_progress_student.models import Student_Progress
from .serializers import TeacherSerializer
from app_progress_student.serializers import StudentProcessSerializer
from utils.utils import teacher_analysis

# Create your views here.

class TeacherCreateListView(APIView):
    def post(self, request):
        try:
            serializer = TeacherSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request):
        try:
            teacher = Teacher.objects.all()
            serializer = TeacherSerializer(teacher, many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({'message':'Data not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request):
        try:
            teacher = Teacher.objects.all()
            if teacher.exists():
                teacher.delete()
                return Response({'message':'Successfully Deleted the Teachers records'}, status=status.HTTP_200_OK)
            else:
                return Response({'message':'No record found'}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 



class GetUpdateDelete_ID(APIView):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(teacher_id = teacher_id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({'message':'Data not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(teacher_id = teacher_id)
            serializer = TeacherSerializer(teacher, data=request.data, partial=True)

            # check if the department id exist else list the existing ids
            department_id = request.data.get('department_id')
            if department_id and not Department.objects.filter(department_id=department_id).exists():
                    department_lst = Department.objects.values_list('department_id','department_name')
                    return Response({'message':f'Id not found choose from {department_lst}'})
            
            if department_id:
                pass
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'error': 'Invalid data', 'details': serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response({'message':'Table not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(teacher_id=teacher_id)
            teacher.delete()
            return Response({'message': f'Teacher with ID {teacher_id} has been successfully deleted.'}, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({'error': f'Teacher with ID {teacher_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class TeacherStudent(APIView):
    def get(self, request, teacher_name=None):
        try:
            if teacher_name:
                teacher_name = Teacher.objects.get(name=teacher_name)
                students = Student_Progress.objects.filter(class_teacher_id = teacher_name)
                serialize = StudentProcessSerializer(students, many =True)

                return Response(serialize.data, status=status.HTTP_200_OK)
            else:
                teacher_name = Teacher.objects.first().name
                students = Student_Progress.objects.annotate(
                    teacher_name=F('class_teacher_id__name')
                ).order_by('teacher_name', 'roll_no')
                serialize = StudentProcessSerializer(students, many =True)
                return Response(serialize.data, status=status.HTTP_200_OK)


        except Student_Progress.DoesNotExist:
            return Response({'error':'Not Found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'An error occurred  while retrieving data from the server', 'details':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeacherAnalysis(APIView):
    def get(self, request, teacher_name=None):
        try:
            if teacher_name:
                teacher = Teacher.objects.get(name=teacher_name)
                students = Student_Progress.objects.filter(class_teacher_id = teacher.teacher_id)
                top_10_queryset = Student_Progress.objects.filter(gained_mark__isnull=False).order_by('-gained_mark')
                top_10_list = list(top_10_queryset[:10])

                analysis = teacher_analysis(students, top_10_list)
                return Response({'analysis': analysis}, status=status.HTTP_200_OK)
            
            # else if no teacher_name it will fetch the data from Teacher model
            # only with the performance rate
            else:
                teachers = Teacher.objects.all()
                serialized_teachers = TeacherSerializer(teachers, many=True).data
                
                return Response(serialized_teachers, status=status.HTTP_200_OK)
        
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             return Response({'error': 'An error occurred while retrieving data from the server', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class BestTeacher(APIView):
    def get(self,request):
        try:
            # Get the best teacher based on performance_rate
            best_teacher = Teacher.objects.order_by('-performance_rate').first()     
            if best_teacher:
                # Serialize the best teacher
                serialized_teacher = TeacherSerializer(best_teacher)
                return Response({'best_teacher': serialized_teacher.data}, status=200)
        except:
                    return Response({'message': 'No teachers found.'}, status=404)