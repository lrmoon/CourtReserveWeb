from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

class ReactView(APIView):
    serializer_class = UserProfileSerializer

    def get(self,request):
        output = [{"username": output.username,
                   "firstname": output.firstname,
                   "lastname": output.lastname,
                   "email": output.email}
                   for output in UserProfile.objects.all()]
        return Response(output)
    
    def post(self,request):

        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)