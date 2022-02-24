from django.test import TestCase
from django.urls import reverse, resolve
from django.forms import Form
from vagas.models import Vaga
from django.utils import timezone
from vagas.views import edit_view

class OportunidadesEditViewTest(TestCase):
    """Test to ensure that edit view for a job opportunity works."""

    def setUp(self) -> None:
        self.vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_endereco='Meu endereço',
            empresa_email='meuemail@email.com',
            empresa_site='https://meusite.com.br',
            empresa_telefone_celular='(11) 98765-3201',
            empresa_telefone_comercial='(11) 8765-3201',
            cargo_titulo='Título do cargo',
            cargo_descricao='Descrição do cargo',
            site_referencia='https://sitereferencia.com.br',
            data_hora_entrevista=timezone.now(),
        )
        url = reverse('oportunidades_edit', args=[str(self.vaga.pk)])
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
        self.assertTemplateUsed(self.response, 'oportunidades_edit.html')
    
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
        view = resolve(f'/oportunidades/{str(self.vaga.pk)}/edit')
        self.assertEqual(edit_view.__name__, view.func.__name__)