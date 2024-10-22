from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from django.db import IntegrityError

from utils.utils import teacher_analysis

from .models import Student_Progress
from django.db.models import Q, Avg
from .serializers import *

class StudentCrudOperation(APIView):

    """to enter students data single entity and multiple entity"""
    def post(self, request, *args, **kwargs):
        serialize = StudentProcessSerializer(data = request.data, many=True)
        if serialize.is_valid():
            try:
                serialize.save()
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
        students = Student_Progress.objects.all()

        # Checking  if there are records to delete
        if students.exists():
            students.delete()
            return Response({"message": "All student records deleted successfully!"}, status=HTTP_200_OK)
        else:
            return Response({"error": "No records found to delete!"}, status=HTTP_404_NOT_FOUND)
    


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
            # Fetch the student using roll_no
            student = Student_Progress.objects.get(roll_no=roll_no)
        except Student_Progress.DoesNotExist:
            return Response({"error": "Student not found."}, status=HTTP_404_NOT_FOUND)

        # Get the data from the request
        data = request.data.copy()

        # Check if 'roll_no' is in the request data
        if 'roll_no' in data:
            return Response({"error": "Roll number cannot be edited."}, status=HTTP_400_BAD_REQUEST)

        # Partial update - only update the fields provided in the request
        serializer = StudentProcessSerializer(student, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()  # Save the changes
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




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
class SortByTeacher(APIView):
    def get(self, request, teacher_name):
        try:
            teacher_name = Teacher.objects.get(name=teacher_name)
            students = Student_Progress.objects.filter(class_teacher_id = teacher_name)
            serialize = StudentProcessSerializer(students, many =True)
            return Response(serialize.data, status=HTTP_200_OK)
        except Student_Progress.DoesNotExist:
            return Response({'error':'Not Found'}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'An error occurred while retrieving data from the server', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        

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
                    
                elif filtration == 'best_teacher':
                    try:
                        # Get the best teacher based on performance_rate
                        best_teacher = Teacher.objects.order_by('-performance_rate').first()
                        
                        if best_teacher:
                            # Serialize the best teacher
                            serialized_teacher = TeacherSerializer(best_teacher)
                            return Response({'best_teacher': serialized_teacher.data}, status=200)
                    except:
                        return Response({'message': 'No teachers found.'}, status=404)










            except Exception as e:
                        return Response({
                            'error': 'An error occurred while retrieving the analysis',
                            'details': str(e)
                        }, status=HTTP_500_INTERNAL_SERVER_ERROR)
            
class TeacherAnalysis(APIView):
    def get(self, request, teacher_name=None):
        try:
            if teacher_name:
                teacher = Teacher.objects.get(name=teacher_name)
                students = Student_Progress.objects.filter(class_teacher_id = teacher.employee_id)
                top_10_queryset = Student_Progress.objects.filter(gained_mark__isnull=False).order_by('-gained_mark')
                top_10_list = list(top_10_queryset[:10])

                analysis = teacher_analysis(students, top_10_list)
                return Response({'analysis': analysis}, status=HTTP_200_OK)
            
            # else if no teacher_name it will fetch the data from Teacher model
            # only with the performance rate
            else:
                teachers = Teacher.objects.all()
                serialized_teachers = TeacherSerializer(teachers, many=True).data
                
                return Response(serialized_teachers, status=HTTP_200_OK)
        
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
             return Response({'error': 'An error occurred while retrieving data from the server', 'details': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)