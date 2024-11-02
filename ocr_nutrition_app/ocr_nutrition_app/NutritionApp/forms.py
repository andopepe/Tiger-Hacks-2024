from django import forms  
from .models import UploadImage

class UploadImageForm(forms.Form):
    image = forms.ImageField()