from django.http import HttpResponse, Http404
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello There')

data = [
    {'id':0, 'name': 'image1.jpg' , 'type': 'jpg'},
    {'id':1, 'name' :'notes.txt', 'type': 'txt'},
    {'id':2, 'name': 'image2.jpg ', 'type': 'jpg'}
]
def files(request):
    return render(request , 'files/files.html' , {'files': data})

def file(request , file_id):
    print('File ID:', file_id)
    f = next((item for item in data if item.get('id') == file_id), None)
    # run interation for what we want and if nothing is returned defualt None
    if f:
        return render(request , 'files/file.html', {'file': f})
    else:
        raise Http404('File does nto exist')