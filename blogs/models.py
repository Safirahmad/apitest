from django.db import models
from tinymce.models import HTMLField  # ye import kar liya


class blogs(models.Model):
    heading = models.CharField(max_length=100)
    description = HTMLField()  
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return self.heading
# Create your models here.
