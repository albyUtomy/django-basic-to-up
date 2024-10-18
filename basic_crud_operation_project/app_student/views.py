from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Students
from .serializers import StudentSerializer


class StudentView(APIView):

    def get(self, request):
        students = Students.objects.all()  # Corrected plural for better readability
        serialize = StudentSerializer(students, many=True)
        return Response(serialize.data)

    
    def post(self, request):
        serialize = StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentByID(APIView):
    def get(self, request, p_id):
        student = Students.objects.get( id=p_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, p_id):
        student = Students.objects.get(id=p_id)
        serialize = StudentSerializer(student, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, p_id):
        try:
            # Attempt to get the student object by ID
            student = Students.objects.get(id=p_id)
            name = student.name
            student.delete()
            return Response({"message": f"Deleted {name}"}, status=status.HTTP_204_NO_CONTENT)
        except Students.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    