from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import Note
from .serializers import NoteSerializer
from json import loads
from uuid import uuid4

class NotesBaseViews(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        note = Note(**data)
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            note.id = uuid4().hex
            note.path = "asd"
            return Response({'status': 'success', 'noteID': note.id})
        else:
            return Response({'status': 'failure', 'errors': serializer.errors})

    def get(self, request):
        return Response()

    def delete(self, request):
        return Response()

    def patch(self, request):
        return Response()