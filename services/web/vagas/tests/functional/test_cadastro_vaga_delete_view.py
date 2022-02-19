from django.test import TestCase, Client
from django.utils import timezone
from vagas.models import Vaga

class CadastroVagaDeleteViewTest(TestCase):
    """
    As a user of the website

    I want a page for confirming the exclusion of a job opportunity

    So that I can safely remove a previously registered opportunity
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        GIVEN a previously registered job opportunity

        WHEN I go to /oportunidades/<ID of job opportunity>/delete

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
            data_hora_entrevista='06/04/2022 09:07',
        )

        cls.response = Client().get(f'/oportunidades/{cls.vaga.pk}/delete')
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.vaga.delete()
        cls.response = None
    
    def test_should_see_nome_da_empresa(self) -> None:
        """
        THEN I should see the corresponding name of the company

        :return: None
        """
        self.assertContains(self.response, self.vaga.empresa_nome)
    
    def test_should_see_endereco_da_empresa(self) -> None:
        """
        THEN I should see the corresponding address of the company

        :return: None
        """
        self.assertContains(self.response, self.vaga.empresa_endereco)
    
    def test_should_see_email_da_empresa(self) -> None:
        """
        THEN I should see a corresponding link to the company's email

        :return: None
        """
        self.assertContains(self.response, f'href="mailto:{self.vaga.empresa_email}"')
    
    def test_should_see_site_da_empresa(self) -> None:
        """
        THEN I should see a corresponding link to the company's website

        :return: None
        """
        self.assertContains(self.response, f'href="{self.vaga.empresa_site}"')
    
    def test_should_see_telefone_celular_da_empresa(self) -> None:
        """
        THEN I should see the corresponding cellphone of the company

        :return: None
        """
        self.assertContains(self.response, self.vaga.empresa_telefone_celular)

    def test_should_see_telefone_comercial_da_empresa(self) -> None:
        """
        THEN I should see the corresponding landline of the company

        :return: None
        """
        self.assertContains(self.response, self.vaga.empresa_telefone_comercial)
    
    def test_should_see_cargo_titulo(self) -> None:
        """
        THEN I should see the corresponding job title

        :return: None
        """
        self.assertContains(self.response, self.vaga.cargo_titulo)
    
    def test_should_see_cargo_descricao(self) -> None:
        """
        THEN I should see the corresponding job description

        :return: None
        """
        self.assertContains(self.response, self.vaga.cargo_descricao)
    
    def test_should_see_site_referencia(self) -> None:
        """
        THEN I should see a corresponding link to a reference website

        :return: None
        """
        self.assertContains(self.response, f'href="{self.vaga.site_referencia}"')
    
    def test_should_see_data_e_hora_da_entrevista(self) -> None:
        """
        THEN I should see the corresponding date and time of interview

        :return: None
        """
        self.assertContains(self.response, self.vaga.data_hora_entrevista)
    
    def test_should_see_data_e_hora_do_cadastro(self) -> None:
        """
        THEN I should see the corresponding date and time of registration

        :return: None
        """
        local_datetime = timezone.localtime(self.vaga.data_hora_cadastro)
        self.assertContains(self.response, local_datetime.strftime('%d/%m/%Y %H:%M'))
    
    def test_should_see_button_for_excluding_job_opportunity(self) -> None:
        """
        THEN I should see a button for excluding the corresponding job opportunity

        :return: None
        """
        self.assertContains(self.response, 'type=submit')