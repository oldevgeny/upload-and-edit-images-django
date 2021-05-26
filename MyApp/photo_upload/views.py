from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse_lazy

from .forms import Image_Form, Image_Form_2
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


class Update_Image_View(UpdateView, MultipleObjectMixin):
    queryset = Image_Model.objects
    form_class = Image_Form
    template_name = 'image_updating.html'
    object_list = Image_Model.objects.all()
    context_object_name = 'image'

    def get_success_url(self):
        return reverse_lazy('image_updating', kwargs={'pk': self.get_object().pk})


class Upload_Image_View(CreateView):
    image = Image_Model
    form_class = Image_Form
    success_url = reverse_lazy('list_of_images')
    template_name = 'image_upload.html'
