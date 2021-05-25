from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import Image_Form
from .models import Image_Model

def delete_image(request, pk):
    image_form = Image_Form(request.POST or None)
    if image_form.is_valid():
        image = Image_Model.objects.get(pk=pk)
        image.delete()
    return redirect('list_of_images')

class Image_List_View(ListView):
    model = Image_Model
    template_name = 'list_of_images.html'
    context_object_name = 'images'


class Upload_Image_View(CreateView):
    image = Image_Model
    form_class = Image_Form
    success_url = reverse_lazy('list_of_images')
    template_name = 'image_upload.html'
