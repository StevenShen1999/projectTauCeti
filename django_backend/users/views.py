from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from json import loads
from .models import ExtendedUser

class BaseUserView(APIView):
    #permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(loads(request.body.decode('utf-8'))['status'])
        user = ExtendedUser()
        user.save()
        return Response({'status': 'success'})