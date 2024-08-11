from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from django.conf import settings
from .models import File
from mainProject.serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def index(request, format=None):
    return render(request, 'files/index.html')

def filesAPI(request):
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return JsonResponse({'files': serializer.data})

@api_view(['GET'])
def fileAPI(request, file_id, format=None):
    try:
        data = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FileSerializer(data)
    return Response({'file': serializer.data})
