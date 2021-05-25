from django import forms

from .models import Image_Model


class Image_Form(forms.ModelForm):
    class Meta:
        model = Image_Model
        fields = ('image', 'image_url', 'width', 'height')
