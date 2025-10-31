from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request):
    """
    PUBLIC_INTERFACE
    Returns a simple health check response.

    GET: No parameters.
    Returns:
        200 OK with {"message": "Server is up!"}
    """
    return Response({"message": "Server is up!"}, status=status.HTTP_200_OK)


# PUBLIC_INTERFACE
class NoteListCreateAPIView(generics.ListCreateAPIView):
    """List all notes or create a new note."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a note by ID."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
