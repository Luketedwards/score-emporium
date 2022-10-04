from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home/index.html")
