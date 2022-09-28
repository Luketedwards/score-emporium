from django.test import TestCase, RequestFactory, Client 
from django.contrib.auth.models import User

from .views import make_request

# Create your tests here.

class TestViews(TestCase):
    def test_get_requests_page(self):
        page = self.client.get("/requests/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "voting/requests2.html")

     