from django.db import models


class Image(models.Model):
    time = models.DateTimeField(auto_now=True, verbose_name="Uploading date")
    image = models.ImageField(upload_to='', null=True, blank=True)
    image_url = models.URLField(max_length=200, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
