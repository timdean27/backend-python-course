from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
from .models import File
from mainProject.serializers import FileSerializer

def index(request):
    return render(request, 'files/index.html')

def filesAPI(request):
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return JsonResponse({'files': serializer.data})

