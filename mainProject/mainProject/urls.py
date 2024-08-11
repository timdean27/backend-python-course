"""
URL configuration for mainProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainProject import views #used for out HTML
from django.conf import settings
from django.conf.urls.static import static
from mainProject import viewsAPI  # Import viewsAPI for our API
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('files/', views.files, name='files'),
    path('files/<int:file_id>/', views.file, name='file'),
    path('files/edit/<int:file_id>/', views.edit, name='edit'),
    path('files/delete/<int:file_id>/', views.delete, name='delete'),
    path('files/upload', views.upload, name='upload'),
    # now using viewsAPI for the api and leaving views for the html
    path('api/files/', viewsAPI.filesAPI, name='api_files'),
    path('api/files/<int:file_id>/', viewsAPI.fileAPI, name='api_file_detail'), 
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
