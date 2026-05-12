"""
this drfProject is made for CRUD api to learn about '
RestAPI

Step1
Standard library: import os,
third Party library, 
local library
"""
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status

from .models import Student
from .serializer import StudentSerializer
from .global_msg import MESSAGE

class TestApiView(APIView):
    """
    this class show GET POST PUT PATCH
    """
    def get(self, request):
        '''
         #accept all complex data or query set or model instance
         # serializer which convert the complex data to the native python 
         #json
        serializer which convert the complex data to the native python 
        '''
        abc=Student.objects.all()
        serializer=StudentSerializer(abc, many=True)
        return Response({MESSAGE:serializer.data})
    def post(self, request):
        """
        native python --> complex data
        """
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({MESSAGE:"Sucessfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({MESSAGE:serializer.errors},status=status.HTTP_403_FORBIDDEN)
        
    def put(self, request,id):
        instance=Student.objects.get(id=id)
        serializer=StudentSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({MESSAGE:"update Sucessfully!!"})
        else:
            return Response({MESSAGE:serializer.errors},status=status.HTTP_403_FORBIDDEN)

    def patch(self, request,id):
        instance=Student.objects.get(id=id)
        serializer=StudentSerializer(instance=instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({MESSAGE:"update Sucessfully!!"})
        else:
            return Response({MESSAGE:serializer.errors},status=status.HTTP_403_FORBIDDEN)

    def delete(self, request,id):
        try:
            data=Student.objects.get(id=id)
            data.delete()
            return Response({MESSAGE:"delete Sucessfully!!"})
        except Student.DoesNotExist:
            return Response({MESSAGE:"data is already deleted"}, status=status.HTTP_404_NOT_FOUND)
        