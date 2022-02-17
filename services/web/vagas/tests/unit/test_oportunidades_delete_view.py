from django.test import SimpleTestCase
from django.urls import reverse
from vagas.models import Vaga

class OportunidadesDeleteViewTest(SimpleTestCase):
    """Test to ensure delete view works correctly."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_endereco='Meu endereço',
            empresa_email='meuemail@email.com',
            empresa_site='https://meusite.com.br',
            empresa_telefone_celular='(11) 98765-3201',
            empresa_telefone_comercial='(11) 8765-3201',
            cargo_titulo='Título do cargo',
            cargo_descricao='Descrição do cargo',
            site_referencia='https://sitereferencia.com.br',
            data_hora_entrevista='04/05/2022 09:03',
        )
    
    def test_url_exists_at_proper_location(self) -> None:
        """
        Ensure that the URL exists at the proper location

        :return: None
        """
        response = self.client.get(f'/oportunidades/{self.vaga.pk}/delete')
        self.assertEqual(200, response.status_code)
    
    def test_view_url_accessible_by_name(self) -> None:
        """
        Ensure that the URL is accessible by name

        :return: None
        """
        response = self.client.get(reverse('oportunidades_delete', args=[str(self.vaga.pk)]))
        self.assertEqual(200, response.status_code)
    
    def test_view_uses_correct_template(self) -> None:
        """
        Ensure that the view uses the correct template

        :return: None
        """
        response = self.client.get(reverse('oportunidades_delete', args=[str(self.vaga.pk)]))
        self.assertTemplateUsed(response, 'oportunidades_delete.html')
    
    def test_view_provides_vaga_object(self) -> None:
        """
        Ensure that the view provides a Vaga object to the template

        :return: None
        """
        response = self.client.get(reverse('oportunidades_delete', args=[str(self.vaga.pk)]))
        self.assertIsInstance(response.context['vaga'], Vaga)