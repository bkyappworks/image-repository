from django.test import TestCase, Client
from django.urls import reverse
import image.models

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('image:index')
        self.create_url = reverse('image:create')


    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')

    def test_create(self):
        response = self.client.get(self.create_url)

        self.assertEquals(response.status_code,302)
        # self.assertTemplateUsed(response,'create.html') # response is a 302 so it can't have a template.
        self.assertRedirects(response, '/accounts/login?next=/create', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True) 

