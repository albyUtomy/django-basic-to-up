from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from django.db import IntegrityError

from .models import Student_Progress
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
        * "para_url is the parameter passed from the url it can by id class_teacher or roll number"
    """

    def get(self, request, para_url=None):
        if 'chemistry-mark-list' in request.path:
            list_chemistry_mark = Student_Progress.objects.exclude(chemistry_mark = None)
            serialize = CombinedMarksSerializer(list_chemistry_mark, many=True)

            chemistry_mark = [{'name':student['name'], 'roll_no':student['roll_no'], 'chemistry_mark':student['chemistry_mark']} for student in serialize.data]
            return Response(chemistry_mark,status=HTTP_200_OK)
        

        elif 'maths-mark-list' in request.path:
            list_maths_mark = Student_Progress.objects.exclude(maths_mark = None)
            serialize = CombinedMarksSerializer(list_maths_mark, many=True)

            maths_mark = [{'name':student['name'], 'roll_no':student['roll_no'], 'maths_mark':student['maths_mark']} for student in serialize.data]
            return Response(maths_mark,status=HTTP_200_OK)


        elif 'physics-mark-list' in request.path:
            list_physics_mark = Student_Progress.objects.exclude(physics_mark = None)
            serialize = CombinedMarksSerializer(list_physics_mark, many=True)

            physics_mark = [{'name':student['name'], 'roll_no':student['roll_no'], 'physics_mark':student['physics_mark']} for student in serialize.data]
            return Response(physics_mark,status=HTTP_200_OK)
        



        elif 'sort-by-class_teacher' in request.path:
            try:
                getBy_class_teacher = Student_Progress.objects.order_by('class_teacher')
                serialize = TeacherSortSerializer(getBy_class_teacher, many=True)
                return Response({'sort-by-class-teacher':serialize.data}, status=HTTP_200_OK)
            
            except Student_Progress.DoesNotExist:
                return Response({'error':'No Teacher Found'}, status=HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error':'An error occurred while retrieving data from the server', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


        elif 'class_teacher' in request.path:
            try:
                sortBy_class_teacher = Student_Progress.objects.filter(class_teacher = para_url)
                serialize = TeacherSortSerializer(sortBy_class_teacher, many=True)
                return Response({'sort-by-class-teacher':serialize.data}, status=HTTP_200_OK)
            except Student_Progress.DoesNotExist:
                return Response({'error':'No Teacher Found'}, status=HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error':'An error occurred while retrieving data from the server', 'details':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class StudentMarkFiltration(APIView):

    """method to filter the list based on:
        * average total mark
        * average chemistry mark
        * average maths mark
        * average physics mark
        * average percentage
        * top 5 students
        * failed students
    """
    def get(sef, request):
        pass