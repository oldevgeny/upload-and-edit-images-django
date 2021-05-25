from django.db import models
from django.conf import settings

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Image_Model(models.Model):
    time = models.DateTimeField(auto_now=True, verbose_name="Uploading date")
    image = models.ImageField(upload_to='', null=True, blank=True)
    image_url = models.URLField(max_length=200, blank=True)
    width = IntegerRangeField(default=200, blank=True, min_value=50, max_value=400)
    height = IntegerRangeField(default=200, blank=True, min_value=50, max_value=400)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
