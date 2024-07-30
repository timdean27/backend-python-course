from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello There')

def files(request):
    return render(request , 'files/files.html' , {'data': 'test-data'})