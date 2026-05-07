from rest_framework.views import APIView
from rest_framework.response import  Response

from .models import Student
from .serializer import StudentSerializer


class TestApiView(APIView):
    def get(self, request):
        abc=Student.objects.all() #accept all complex data or query set or model instance
        serializer=StudentSerializer(abc, many=True) # serializer which convert the complex data to the native python 
        return Response({'message':serializer.data}) #json
    
    
    
    """
    [database(complex_data)-> native python ] serialization 
    why this is done?  so that it could be easily render into json.
    """

    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'message':"Sucessfully"})
