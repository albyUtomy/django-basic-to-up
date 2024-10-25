from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Teacher
from .serializers import TeacherSerializer

# Create your views here.

class TeacherCreateListView(APIView):
    def post(self, request):
        try:
            serializer = TeacherSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TeacherUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'teacher_id'

    def update(self,request, *args, **kwargs):
        kwargs['partial'] = True
        return super.update(request, *args, **kwargs)