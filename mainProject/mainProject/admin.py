from django.contrib import admin
from mainProject.models import File

# creating a class to show read only atribuits in admin page such as timestamp
class FileAdmin(admin.ModelAdmin):
    readonly_fields=('id', 'upload_timestamp')

admin.site.register(File , FileAdmin)