from django.db import models

# Create your models here.
# configure for file
class Image(models.Model):
    file = models.FileField(upload_to = 'file')
