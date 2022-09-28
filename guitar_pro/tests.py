from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):
    
    def test_get_guitar_pro_page(self):
        page = self.client.get("/GP/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "guitar_pro/score_player.html")