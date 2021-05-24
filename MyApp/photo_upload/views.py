from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import Image_Form
from .models import Image

def delete_image(request, pk):
    if request.method == 'POST':
        image = Image.objects.get(pk=pk)
        image.delete()
    return redirect('list_of_images')

class Image_List_View(ListView):
    model = Image
    template_name = 'list_of_images.html'
    context_object_name = 'images'


class Upload_Image_View(CreateView):
    image = Image
    form_class = Image_Form
    success_url = reverse_lazy('list_of_images')
    template_name = 'image_upload.html'
