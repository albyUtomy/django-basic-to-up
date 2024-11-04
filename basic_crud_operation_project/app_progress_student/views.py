from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from utils.utils import teacher_analysis

from .models import Student_Progress
from django.db.models import Q, Avg
from django.db.models import F
from django.db import IntegrityError

from .serializers import *



class StudentCrudOperation(APIView):

    """to enter students data single entity and multiple entity"""
    def post(self, request, *args, **kwargs):
        serialize = StudentProcessSerializer(data = request.data, many=True)
        if serialize.is_valid():
            try:
                for student in request.data:
                    school_id = student.get('school_id')
                    department_id = student.get('department_id')
                    teacher_id = student.get('class_teacher_id')

                    print(">>>>>>>>>>>>>>>>>>>>>>>>",department_id, school_id, teacher_id)

                    if teacher_id and department_id:
                        print(department_id)
                        teacher = Teacher.objects.filter(department_id=department_id)
                        print(">>>>>>>>>>>>>",teacher)
                        department = Department.objects.get(hod_name__teacher_id=teacher_id)
                        print(">>>>>>>>>>",department)

                return Response(serialize.data, status=HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({'error':'Student Roll Number Already Exist'}, status=HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error':'An error occurred while saving', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serialize.errors, status=HTTP_400_BAD_REQUEST)
        
    """to get all the students list"""
    def get(self,request):
        try:
            list_students = Student_Progress.objects.all()
            serialize =StudentProcessSerializer(list_students, many=True)
            return Response(serialize.data)
        except Exception as e:
            return Response({'error':'An error occurred while retrieving students list', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


    """to delete all the students records"""
    def delete(self, request):
        try:
            students = Student_Progress.objects.all()

            # Checking  if there are records to delete
            if students.exists():
                students.delete()
                return Response({"message": "All student records deleted successfully!"}, status=HTTP_200_OK)
        except Student_Progress.DoesNotExist:
                return Response({"error": "No records found to delete!"}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    


class StudentModification(APIView):
    # retrieving student with roll number
    def get(self, request, roll_no):
        try:
            student = Student_Progress.objects.get(roll_no=roll_no)
            serializer = StudentProcessSerializer(student)
            return Response(serializer.data, status=HTTP_200_OK)
        except Student_Progress.DoesNotExist:
            return Response({'error':'Student with this roll number does not exist.'}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'An error occurred while retrieving data from the server', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        

    # update the details using roll number
    def put(self, request, roll_no):
        try:
            student = Student_Progress.objects.get(roll_no=roll_no)
            serializer = StudentProcessSerializer(student, data=request.data, partial=True)
            
            if serializer.is_valid():
                print(serializer)
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            
        except Student_Progress.DoesNotExist:
            return Response({'error': 'Student not found'}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'An error occurred while retrieving data from the server', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        


    # delete a student details using roll number
    def delete(self, request, roll_no):
        try:
            student = Student_Progress.objects.get(roll_no=roll_no)
            name = student.name
            student.delete()
            return Response({'message':f'Delete {name}'}, status=HTTP_204_NO_CONTENT)
        except Student_Progress.DoesNotExist:
            return Response({"error":"Student not found"}, status=HTTP_400_BAD_REQUEST)
        

class StudentSortedBy(APIView):
    """function to sort the student details based on :
        * chemistry mark list
        * maths mark list
        * physics mark list
        * ordered by class teacher name
        * list the student of specific class teacher
        * "subject is the parameter passed from the url it can by id class_teacher or roll number"
    """

    def get(self, request, subject=None):
        if subject == 'chemistry':
            list_chemistry_mark = Student_Progress.objects.exclude(chemistry_mark = None)
            serialize = CombinedMarksSerializer(list_chemistry_mark, many=True)

            chemistry_mark = [{'name':student['name'], 'roll_no':student['roll_no'], 'chemistry_mark':student['chemistry_mark']} for student in serialize.data]
            return Response(chemistry_mark,status=HTTP_200_OK)
        
        elif subject== 'maths':
            list_maths_mark = Student_Progress.objects.exclude(maths_mark = None)
            serialize = CombinedMarksSerializer(list_maths_mark, many=True)

            maths_mark = [{'name':student['name'], 'roll_no':student['roll_no'], 'maths_mark':student['maths_mark']} for student in serialize.data]
            return Response(maths_mark,status=HTTP_200_OK)


        elif subject== 'physics':
            list_physics_mark = Student_Progress.objects.exclude(physics_mark = None)
            serialize = CombinedMarksSerializer(list_physics_mark, many=True)

            physics_mark = [{'name':student['name'], 'roll_no':student['roll_no'], 'physics_mark':student['physics_mark']} for student in serialize.data]
            return Response(physics_mark,status=HTTP_200_OK)
        

# Sort by class teacher
        

class StudentMarkStatistic(APIView):
    def get(self, request, filtration=None):
            try:
                if filtration == 'average-marks' in request.path:
                    try:

                        # Fetching marks from the database
                        avg_data = Student_Progress.objects.aggregate(
                        average_chemistry_mark=Avg('chemistry_mark'),
                        average_physics_mark=Avg('physics_mark'),
                        average_maths_mark=Avg('maths_mark'),
                        average_gained_total=Avg('gained_mark'),
                        average_percentage=Avg('percentage')
                    )
                        # Return the response with the aggregated data
                        return Response({'average': avg_data}, status=HTTP_200_OK)
                    except:
                        return Response({"error":"Statistics not found"}, status=HTTP_400_BAD_REQUEST)

            
                elif filtration == 'report-failed':
                    try:
                        students= Student_Progress.objects.all()
                        failed_students = students.filter(
                        Q(chemistry_mark__lt=40) | 
                        Q(physics_mark__lt=40) | 
                        Q(maths_mark__lt=40)
                        
                    )
                        serialize = CombinedMarksSerializer(failed_students, many=True)
                        return Response({
                            'failed_students': serialize.data
                            }, status=HTTP_200_OK)
                    except:
                        return Response({"error":"Failed Report is not found"}, status=HTTP_400_BAD_REQUEST)


                elif filtration == 'top5':
                    try:
                        top_students = Student_Progress.objects.filter(gained_mark__isnull=False).order_by('-gained_mark')[:5]
                        serialize = CombinedMarksSerializer(top_students, many=True)
                        return Response({'top_students': serialize.data}, status=HTTP_200_OK)
                    except:
                        return Response({"error":"Topers List is not found"}, status=HTTP_400_BAD_REQUEST)   

            except Exception as e:
                        return Response({
                            'error': 'An error occurred while retrieving the analysis',
                            'details': str(e)
                        }, status=HTTP_500_INTERNAL_SERVER_ERROR)
            
            
            
class ActiveOrNot(APIView):
    def get(self,request):
        students = Student_Progress.objects.filter(is_active=True)
        serializers =StudentProcessSerializer(students, many=True)
        return Response({'message': serializers.data}, status=HTTP_200_OK)