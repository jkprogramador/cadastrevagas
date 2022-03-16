from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.forms import Form
from vagas.views import create_view

class OportunidadesNewViewTest(SimpleTestCase):
    """Test to ensure that view for new job opportunities works."""

    def setUp(self) -> None:
        url = reverse('oportunidades_new')
        self.response = self.client.get(url)

    def test_status_code(self) -> None:
        """
        Ensure that the view returns correct status code.
        
        :rtype: None
        """
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self) -> None:
        """
        Ensure that the view uses the correct template.

        :rtype: None
        """
        self.assertTemplateUsed(self.response, 'oportunidades_new.html')
    
    def test_provides_form_object(self) -> None:
        """
        Ensure that the view provides a form object to the template.

        :rtype: None
        """
        self.assertIsInstance(self.response.context['form'], Form)
    
    def test_url_resolves_to_correct_view(self) -> None:
        """
        Ensure that the given URL path resolves to the correct view.

        :rtype: None
        """
        view = resolve('/oportunidades/new')
        self.assertEqual(create_view.__name__, view.func.__name__)