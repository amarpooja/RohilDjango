from django.contrib import admin
from .models import ImageTable

@admin.register(ImageTable)
class ImageAdmin(admin.ModelAdmin):
    list_display =['id','image','desc','date']