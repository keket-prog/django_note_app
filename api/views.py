from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note

from .serializers import NoteSerializer
from api import serializers
# Create your views here.

@api_view(['GET']) # HTTP request that are allowed
def getRoutes(request):
   routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
   return Response(routes)


# get all data from DB and return it
@api_view(['GET'])
def getNotes(request):
      # get the list of python objects from the DB, the cannot be passed to the Response
      # these still need to be serialised - convered from python object to JSON
      notes = Note.objects.all().order_by('-updated') # order by the latest update
      serializer = NoteSerializer(notes, many=True) # convers data
      return Response(serializer.data) # retruns data

# get one note from the DB and retrun it 
@api_view(['GET'])
def getNote(request,pk):
      # get the list of python objects from the DB, the cannot be passed to the Response
      # these still need to be serialised - convered from python object to JSON
      notes = Note.objects.get(id=pk)
      serializer = NoteSerializer(notes, many=False) # convers a single record
      return Response(serializer.data) # retruns data      

@api_view(['POST'])
def createNote(request):
   noteData = request.data
   note = Note.objects.create(
      body=noteData['body']
   )
   serializer =NoteSerializer(note, many=False)
   return Response(serializer.data)
   
# update note route
@api_view(['PUT'])
def updateNote(request, pk):
      noteData = request.data
      note  = Note.objects.get(id=pk)
      serializer = NoteSerializer(instance=note, data=noteData)

      if serializer.is_valid():
         serializer.save()
      return Response(serializer.data)   


@api_view(['DELETE'])
def deleteNote(request, pk):

   note = Note.objects.get(id=pk)
   note.delete()
   return Response('Note was deleted')      


