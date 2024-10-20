from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from django.db import IntegrityError

from utils.utils import get_average, teacher_analysis

from .models import Student_Progress
from django.db.models import Q
from .serializers import *

class StudentCrudOperation(APIView):

    """to enter students data single and bulk"""
    def post(self, request, *args, **kwargs):
        serialize = StudentProcessSerializer(data = request.data, many=True)
        if serialize.is_valid():
            try:
                serialize.save()
                return Response(serialize.data, status=HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({'error':'Student Roll Number Already Exist'}, status=HTTP_400_BAD_REQUEST)
            except Exception as e:
                # Handle any other unforeseen errors
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
            student = Student_Progress.objects.get(roll_no=roll_no)
        except Student_Progress.DoesNotExist:
            return Response({"error": "Data Not Found"}, status=HTTP_404_NOT_FOUND)

        serialize = StudentProcessSerializer(student, data=request.data)

        if serialize.is_valid():
            new_roll = serialize.validated_data.get('roll_no', roll_no)  # Fetch new roll number

            # Check if the new roll number is different
            if new_roll != roll_no:
                # Check if a student with the new roll number already exists
                if Student_Progress.objects.filter(roll_no=new_roll).exists():
                    return Response({'error': "Roll number already exists"}, status=HTTP_400_BAD_REQUEST)


                """
                Delete the old student record before saving only if the roll id diffrnt
                Create a new student record with the updated roll number
                Copy validated data
                Set the new roll number
                """
    
                student.delete()
                new_student_data = serialize.validated_data.copy()
                new_student_data['roll_no'] = new_roll 

                """Create and save the new student instance"""
                new_student = Student_Progress(**new_student_data)
                new_student.save()
                return Response(StudentProcessSerializer(new_student).data, status=HTTP_201_CREATED)  # 201 Created for new entry
            else:
                serialize.save()
                return Response(serialize.data, status=HTTP_200_OK)
        else:
            return Response(serialize.errors, status=HTTP_400_BAD_REQUEST)


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
    def get(self, request, teacher_name=None):
        try:
            teacher_name = Student_Progress.objects.filter(class_teacher=teacher_name)
            serialize = TeacherSortSerializer(teacher_name, many=True)
            return Response(serialize.data, status=HTTP_200_OK)
        except Student_Progress.DoesNotExist:
            return Response({'error':'Not Found'}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'An error occurred while retrieving data from the server', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        

class StudentMarkStatistic(APIView):
    def get(self, request, filtration=None):
        if filtration == 'average-marks' in request.path:
            try:
                # Fetching marks from the database
                physics_marks = list(Student_Progress.objects.values_list('physics_mark', flat=True))
                maths_marks = list(Student_Progress.objects.values_list('maths_mark', flat=True))
                chemistry_marks = list(Student_Progress.objects.values_list('chemistry_mark', flat=True))
                gained_marks = list(Student_Progress.objects.values_list('gained_mark', flat=True))
                percentage = list(Student_Progress.objects.values_list('percentage', flat=True))

                # Calculating averages
                avg_data = {
                    "average_chemistry_mark": get_average(chemistry_marks),
                    "average_physics_mark": get_average(physics_marks),
                    "average_maths_mark": get_average(maths_marks),
                    "average_gained_total":get_average(gained_marks),
                    "average_percentage": get_average(percentage)
                }

                return Response({'average': avg_data}, status=HTTP_200_OK)

            except Exception as e:
                return Response({
                    "error": "An error occurred while fetching averages.",
                    "details": str(e)
                }, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
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
            
            except Exception as e:
                return Response({
                'error': 'An error occurred while retrieving data failed students record.',
                'details': str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)

        
        elif filtration == 'top5':
            try:
                top_students = Student_Progress.objects.filter(gained_mark__isnull=False).order_by('-gained_mark')[:5]
                serialize = CombinedMarksSerializer(top_students, many=True)
                return Response({'top_students': serialize.data}, status=HTTP_200_OK)

            except Exception as e:
                return Response({
                    'error': 'An error occurred while retrieving data.',
                    'details': str(e)
                }, status=HTTP_500_INTERNAL_SERVER_ERROR)
            
        elif filtration == 'teacher-analysis':
            try:
                analysis_result = teacher_analysis(Student_Progress)
                return Response(analysis_result, status=HTTP_200_OK)
            except Exception as e:
                return Response({
                    'error': 'An error occurred while retrieving the analysis',
                    'details': str(e)
                }, status=HTTP_500_INTERNAL_SERVER_ERROR)