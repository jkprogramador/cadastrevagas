from django.test import TestCase
from django.urls import reverse, resolve
from vagas.views import index

class HomepageViewTest(TestCase):
    """Ensure that the homepage view works correctly"""

    def setUp(self) -> None:
        url = reverse('homepage')
        self.response = self.client.get(url)

    def test_status_code(self) -> None:
        """
        Ensure that the view returns the correct status code.

        :rtype: None
        """
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self) -> None:
        """
        Ensure that the view uses the correct template.

        :rtype: None
        """
        self.assertTemplateUsed(self.response, 'homepage.html')
    
    def test_url_resolves_to_correct_view(self) -> None:
        """
        Ensure that the given URL path resolves to the correct view.

        :rtype: None
        """
        view = resolve('/')
        self.assertEqual(index.__name__, view.func.__name__)