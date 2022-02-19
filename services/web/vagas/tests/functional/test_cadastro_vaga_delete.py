from django.test import TestCase, Client
from django.urls import reverse
from vagas.models import Vaga

class CadastroVagaDeleteTest(TestCase):
    """
    As a user of the website

    I want to remove a previously registered job opportunity

    So that I keep the most relevant job opportunities only
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        GIVEN a previously registered job opportunity

        WHEN I submit a form to /oportunidades/<ID of job opportunity>/delete

        :return: None
        """
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
            data_hora_entrevista='07/05/2022 09:08',
        )

        cls.response = Client().post(f'/oportunidades/{cls.vaga.pk}/delete', follow=True)
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.vaga.delete()
        cls.response = None
    
    def test_should_delete_job_opportunity(self) -> None:
        """
        THEN it should remove the corresponding job opportunity

        :return: None
        """
        with self.assertRaises(Vaga.DoesNotExist):
            Vaga.objects.get(pk=self.vaga.pk)
    
    def test_should_redirect_to_homepage(self) -> None:
        """
        THEN it should redirect to the homepage

        :return: None
        """
        self.assertRedirects(self.response,
            reverse('homepage'), status_code=302, target_status_code=200
        )
    
    def test_should_show_success_message(self) -> None:
        """
        THEN it should show a success message confirming the removal of the job opportunity

        :return: None
        """
        self.assertContains(self.response, 'Vaga removida com sucesso.')