# pip install django-utils-six
# pip install Pillow
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.core.files import File
from django.utils.six import BytesIO

import image.models

from PIL import Image
from io import StringIO

def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
   """
   Generate a test image, returning the filename that it was saved as.

   If ``storage`` is ``None``, the BytesIO containing the image data
   will be passed instead.
   """
   data = BytesIO()
   Image.new(image_mode, size).save(data, image_format)
   data.seek(0)
   if not storage:
       return data
   image_file = ContentFile(data.read())
   return storage.save(filename, image_file)

class TestModels(TestCase):
    def setUp(self):
        super(TestModels, self).setUp()
    def test_valid_form(self):
        '''
        valid post data should redirect
        The expected behavior is to show the image
        '''
        url = reverse('image:create')
        avatar = create_image(None, 'avatar.png')
        avatar_file = SimpleUploadedFile('front.png', avatar.getvalue())
        data = {'image': avatar_file}
        response = self.client.post(url, data, follow=True)

        self.assertEquals(response.status_code, 200)