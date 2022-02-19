from django.test import SimpleTestCase
from django.urls import reverse

class HomepageViewTest(SimpleTestCase):
    """Ensure that the homepage view works correctly"""

    def test_view_url_exists_at_proper_location(self) -> None:
        """
        Ensure that the URL for the view exists.

        :return: None
        """
        response = self.client.get('')
        self.assertEqual(200, response.status_code)
    
    def test_view_url_accessible_by_name(self) -> None:
        """
        Ensure that the URL is accessible by name.

        :return: None
        """
        response = self.client.get(reverse('homepage'))
        self.assertEqual(200, response.status_code)
    
    def test_view_uses_correct_template(self) -> None:
        """
        Ensure that the view uses the correct template.

        :return: None
        """
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')