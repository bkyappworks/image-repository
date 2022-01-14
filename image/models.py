from django.db import models
from .formatChecker import ContentTypeRestrictedFileField

# Create your models here.
# configure for file
class Image(models.Model):
    # file = models.FileField(upload_to = 'file')
    file = ContentTypeRestrictedFileField(upload_to='file',max_upload_size=5242880,blank=True, null=True)
