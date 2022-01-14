from django.test import SimpleTestCase
from django.urls import reverse,resolve
import image.views

# python manage.py test image
class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('image:index')
        print(resolve(url))
        self.assertEquals(resolve(url).func,image.views.index)

    def test_create_url_resolves(self):
        url = reverse('image:create')
        print(resolve(url))
        self.assertEquals(resolve(url).func,image.views.create)
