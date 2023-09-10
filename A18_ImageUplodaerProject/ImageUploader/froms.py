from django import forms
from .models import ImageTable

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageTable
        fields = '__all__'