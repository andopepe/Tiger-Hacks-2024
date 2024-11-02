from django.db import models

# Create your models here.
class UploadImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/') # Specify directory to fill.

    def __str__(self):
        return self.title