from django.test import SimpleTestCase
from django.urls import reverse
from django.forms import Form

class OportunidadesNewViewTest(SimpleTestCase):
    """Test to ensure that view for new job opportunities works."""

    def test_view_url_exists_at_proper_location(self) -> None:
        """
        Ensure that the URL for the view exists.
        
        :return: None
        """
        response = self.client.get('/oportunidades/new')
        self.assertEqual(200, response.status_code)
    
    def test_view_url_accessible_by_name(self) -> None:
        """
        Ensure that the URL is accessible by name.

        :return: None
        """
        response = self.client.get(reverse('oportunidades_new'))
        self.assertEqual(200, response.status_code)
    
    def test_view_uses_correct_template(self) -> None:
        """
        Ensure that the view uses the correct template.

        :return: None
        """
        response = self.client.get(reverse('oportunidades_new'))
        self.assertTemplateUsed(response, 'oportunidades_new.html')
    
    def test_view_provides_form_object(self) -> None:
        """
        Ensure that the view provides a form object to the template.

        :return: None
        """
        response = self.client.get(reverse('oportunidades_new'))
        self.assertIsInstance(response.context['form'], Form)