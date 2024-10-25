from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from .models import School
from .serializers import SchoolSerializer

import logging
logger = logging.getLogger(__name__)

class SchoolCrud(APIView):
    def post(self, request):
        try:
            serializer = SchoolSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':serializer.data},status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating school: {e}" )
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def get(self, request):
        try:
            school = School.objects.all()
            serializer = SchoolSerializer(school, many=True)

            return Response(serializer.data,status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({'error':'Schools data is not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
