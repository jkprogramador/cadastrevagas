from django.test import SimpleTestCase
from django.urls import reverse
from vagas.models import Vaga

class OportunidadesDetailViewTest(SimpleTestCase):
    """Test to ensure that detail view for a job opportunity works."""

    @classmethod
    def setUpClass(cls) -> None:
        cls._vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_endereco='Meu endereço',
            empresa_email='meuemail@email.com',
            empresa_site='https://meusite.com.br',
            empresa_telefone_celular='(11) 98765-3201',
            empresa_telefone_comercial='(11) 8765-3201',
            cargo_titulo='Título do cargo',
            cargo_descricao='Descrição do cargo',
            site_referencia='https://sitereferencia.com.br',
            data_hora_entrevista='20/01/2022 15:30',
        )
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls._vaga.delete()

    def test_view_url_exists_at_proper_location(self) -> None:
        """
        Ensure that the URL for the view exists.

        :return: None
        """
        response = self.client.get(f'/oportunidades/{self._vaga.id}')
        self.assertEqual(200, response.status_code)
    
    def test_view_url_accessible_by_name(self) -> None:
        """
        Ensure that the URL is accessible by name.

        :return: None
        """
        response = self.client.get(reverse('oportunidades_detail', args=[str(self._vaga.id)]))
        self.assertEqual(200, response.status_code)
    
    def test_view_uses_correct_template(self) -> None:
        """
        Ensure that the view uses the correct template.

        :return: None
        """
        response = self.client.get(reverse('oportunidades_detail', args=[str(self._vaga.id)]))
        self.assertTemplateUsed(response, 'oportunidades_detail.html')
    
    def test_view_provides_vaga_object(self) -> None:
        """
        Ensure that the view provides a Vaga object to the template.

        :return: None
        """
        response = self.client.get(reverse('oportunidades_detail', args=[str(self._vaga.id)]))
        self.assertIsInstance(response.context['vaga'], Vaga)