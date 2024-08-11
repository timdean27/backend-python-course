from django.http import Http404, JsonResponse  # Import necessary classes for handling HTTP errors and JSON responses
from django.shortcuts import redirect, render  # Import utilities for rendering templates and redirecting requests
from rest_framework.views import APIView  # Import APIView for creating class-based views (though it's not used here)
from django.conf import settings  # Import settings for accessing configuration values
from .models import File  # Import the File model
from mainProject.serializers import FileSerializer  # Import the serializer for the File model
from rest_framework.response import Response  # Import Response for handling API responses
from rest_framework.decorators import api_view, permission_classes # Import the api_view decorator for handling HTTP methods and permission classes for decorator 
from rest_framework import status  # Import status codes for API responses
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated permission class

def index(request, format=None):
    return render(request, 'files/index.html')  # Renders the index.html template

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def filesAPI(request):

    if request.method == 'GET':
        data = File.objects.all()  # Retrieve all File objects from the database
        serializer = FileSerializer(data, many=True)  # Serialize the file data
        return Response({'files': serializer.data})  # Return the serialized data as JSON

    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data)  # Deserialize the request data into a FileSerializer instance
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new file instance to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the serialized data with a 201 Created status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors with a 400 Bad Request status


# PATCH is used for making partial updates to a resource. 
# When using PATCH, you only send the fields that you want to update.
# PUT is used to update a resource or create it if it does not exist. 
# When using PUT, you typically send the complete representation of the resource.
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def fileAPI(request, file_id, format=None):
    try:
        data = File.objects.get(pk=file_id)  # Retrieve the file object with the given ID
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # Return a 404 Not Found status if the file does not exist
    
    if request.method == 'GET':
        serializer = FileSerializer(data)  # Serialize the file data
        return Response({'file': serializer.data})  # Return the serialized data

    elif request.method == 'PATCH':
        serializer = FileSerializer(data, data=request.data, partial=True)  # Deserialize the request data into the existing FileSerializer instance, allowing partial updates
        if serializer.is_valid():  # Check if the data is valid returns true
            serializer.save()  # Save the updated file instance
            return Response(serializer.data)  # Return the updated data

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors with a 400 Bad Request status

    elif request.method == 'DELETE':
        data.delete()  # Delete the file instance from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return a 204 No Content status indicating successful deletion
