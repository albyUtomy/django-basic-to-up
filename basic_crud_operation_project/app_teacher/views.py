from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F

from .models import Teacher
from app_department.models import Department
from app_progress_student.models import Student_Progress
from app_school.models import School
from .serializers import TeacherSerializer
from app_progress_student.serializers import StudentDetail
from utils.utils import teacher_analysis


from django.shortcuts import get_object_or_404

# Create your views here.




class TeacherCreateListView(APIView):
    def post(self, request):

        
        # With out any custom validation
        try:
            serializer = TeacherSerializer(data=request.data, many=True)
            if serializer.is_valid():

                """ 
                # validation logic
                for teacher in request.data:
                    department_id = teacher.get('department_id')
                    school_id = teacher.get('school_id')

                    # Check if the school is active
                    try:
                        school = School.objects.get(school_id=school_id, is_active=True)
                    except School.DoesNotExist:
                        return Response({'error': f"School with ID {school_id} does not exist or is not active."},
                                        status=status.HTTP_400_BAD_REQUEST)

                    # Check if the department exists and is active
                    try:
                        department = Department.objects.get(department_id=department_id, is_active=True)
                    except Department.DoesNotExist:
                        return Response({'error': f"Department with ID {department_id} does not exist or is not active."},
                                        status=status.HTTP_400_BAD_REQUEST)

                    # Check if the department belongs to the specified school
                    if department.school_id != school:
                        d_filter = Department.objects.filter(school_id=school_id, is_active=True).values('department_name', 'department_id')

                        if not d_filter.exists():
                            return Response({'error': f"School ID: {school_id} has no active departments."}, 
                                            status=status.HTTP_400_BAD_REQUEST)

                        return Response({
                            'error': f"Department with ID {department_id} does not belong to school {school_id} or is not active.",
                            'departments_belonging_to_school': list(d_filter)
                        }, status=status.HTTP_400_BAD_REQUEST)

                # Save the serializer data after all checks are successful

                """
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        

    def get(self, request):
        try:
            teacher = Teacher.active_objects.all()
            serializer = TeacherSerializer(teacher, many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({'message':'Data not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class GetUpdateDelete_ID(APIView):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.active_objects.filter(teacher_id=teacher_id).first()
            print("teacher",teacher)
            if teacher:
                serializer = TeacherSerializer(teacher)
                print("serializer.data",serializer.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Teacher is inactive'}, status=status.HTTP_403_FORBIDDEN)
        except Teacher.DoesNotExist:
            return Response({'message':'Data not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(teacher_id = teacher_id)
            serializer = TeacherSerializer(teacher, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid data', 'details': serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response({'message':'Table not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    # def delete(self, request, teacher_id):
    #     try:
    #         teacher = Teacher.objects.get(teacher_id=teacher_id)
    #         teacher.delete()
    #         return Response({'message': f'Teacher with ID {teacher_id} has been successfully deleted.'}, status=status.HTTP_200_OK)
    #     except Teacher.DoesNotExist:
    #         return Response({'error': f'Teacher with ID {teacher_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class TeacherStudent(APIView):
    def get(self, request, teacher_name=None):
        try:
            if teacher_name:
                teacher_name = Teacher.active_objects.get(name=teacher_name)
                students = Student_Progress.objects.filter(class_teacher_id = teacher_name, is_active=True)
                serialize = StudentDetail(students, many =True)

                return Response(serialize.data, status=status.HTTP_200_OK)
            else:
                active_teachers = Teacher.active_objects.all()
                if active_teachers.exists():
                    # Get all active students assigned to any active teacher
                    students = Student_Progress.objects.filter(
                        class_teacher_id__in=active_teachers, is_active=True
                            ).annotate(teacher_name=F('class_teacher_id__name')).order_by('teacher_name', 'roll_no')
                    serialize = StudentDetail(students, many=True)

                    return Response(serialize.data, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'No active teachers found.'}, status=status.HTTP_404_NOT_FOUND)
        except Student_Progress.DoesNotExist:
            return Response({'error':'Not Found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'An error occurred  while retrieving data from the server', 'details':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeacherAnalysis(APIView):
    def get(self, request, teacher_name=None):
        try:
            if teacher_name:
                teacher = Teacher.active_objects.filter(name=teacher_name).first()
                students = Student_Progress.objects.filter(class_teacher_id = teacher.teacher_id, is_active=True)
                top_10_queryset = Student_Progress.objects.filter(gained_mark__isnull=False, is_active=True).order_by('-gained_mark')
                top_10_list = list(top_10_queryset[:10])

                analysis = teacher_analysis(students, top_10_list)
                return Response({'analysis': analysis}, status=status.HTTP_200_OK)
            
            # else if no teacher_name it will fetch the data from Teacher model
            # only with the performance rate
            else:
                teachers = Teacher.active_objects.all()
                serialized_teachers = TeacherSerializer(teachers, many=True).data
                
                return Response(serialized_teachers, status=status.HTTP_200_OK)
        
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
             return Response({'error': 'An error occurred while retrieving data from the server', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class BestTeacher(APIView):
    def get(self,request):
        try:
            # Get the best teacher based on performance_rate
            best_teacher = Teacher.active_objects.order_by('-performance_rate').first()     
            if best_teacher:
                # Serialize the best teacher
                serialized_teacher = TeacherSerializer(best_teacher)
                return Response({'best_teacher': serialized_teacher.data}, status=200)
        except:
                    return Response({'message': 'No teachers found.'}, status=404)
        

class MakeInactiveView(APIView):
    def get(self, request, teacher_id):
        # Teacher.objects.get(teacher_id=teacher_id).update(is_active=False)
        # Department.objects.get(teacher_id=teacher_id).update(hod_name=None)
        # Student_Progress.objects.get(teacher_id=teacher_id).update(teacher_id=None)

        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        name = teacher.name
        teacher.is_active = False
        teacher.save()

        department = Department.objects.filter(hod_name=teacher, is_active=True).update(hod_name=None)
        students = Student_Progress.objects.filter(class_teacher_id=teacher, is_active=True).update(class_teacher_id=None)

        return Response({'message': f'Teacher {name}, id : {teacher_id} marked as inactive successfully.'}, status=status.HTTP_200_OK)\
        
class ActiveOrInActive(APIView):
    def get(self, request, active_or_not):
        try:
            if active_or_not == 'is_active' in request.path:
                teacher = Teacher.active_objects.all()
                serializer = TeacherSerializer(teacher, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            if  active_or_not == 'is_inactive' in request.path:
                teacher = Teacher.inactive_objects.all()
                serializer = TeacherSerializer(teacher, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                