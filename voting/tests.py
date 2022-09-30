
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .views import make_request

# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        self.client = Client(username='testuser', password='12345')
        self.requests_url = reverse('requests')
        self.make_request_url = reverse('make_request')
        

    def test_get_requests_page(self):
        response = self.client.get(self.requests_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "voting/requests2.html")    

    def test_make_request_page(self):
        response = self.client.get(self.make_request_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "voting/make-a-request.html")
     