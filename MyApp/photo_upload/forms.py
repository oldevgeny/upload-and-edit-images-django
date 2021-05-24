from django import forms

from .models import Image


class Image_Form(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'image_url')
