from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('images/<int:pk>/delete', views.delete_image, name='delete_image'),

    path('images/', views.Image_List_View.as_view(), name='list_of_images'),
    path('images/upload/', views.Upload_Image_View.as_view(), name='class_upload_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
