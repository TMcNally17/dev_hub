from django.test import TestCase


class TestViews(TestCase):
    
    """
    Test correct page is returned using right template
    """
    
    def test_get_blog(self):
        
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog.html")
    