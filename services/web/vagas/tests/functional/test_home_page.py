from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from vagas.models import Vaga

class HomePageTest(TestCase):
    """
    As a user of the website
    
    I want a page that displays job opportunities

    So that I can see all the job opportunities I've registered
    """

    def setUp(self) -> None:
        self.url = reverse('homepage')
        self.vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_endereco='Meu endereço',
            empresa_email='empresa@email.com',
            empresa_site='empresa.com.br',
            empresa_telefone_celular='(11) 96712-0302',
            empresa_telefone_comercial='(11) 8067-2511',
            cargo_titulo='Cargo título',
            cargo_descricao='Cargo descrição',
            site_referencia='www.sitereferencia.com.br',
            data_hora_entrevista=timezone.localtime(),
            situacao=Vaga.Status.REJECTED,
        )
    
    def test_should_have_link_to_homepage(self) -> None:
        """
        GIVEN a homepage for the website

        WHEN I visit it

        THEN it should have a link to the homepage

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertContains(response, f'href="{self.url}"')
    
    def test_should_display_cargo_titulo(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should display the corresponding job title

        :rtype: None
        """

        response = self.client.get(self.url)
        self.assertContains(response, self.vaga.cargo_titulo)
    
    def test_should_display_empresa_nome(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should display the corresponding name of the company

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertContains(response, self.vaga.empresa_nome)
    
    def test_should_display_data_hora_entrevista(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should display the date and time of interview for that opportunity

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertContains(response, self.vaga.data_hora_entrevista.strftime('%d/%m/%Y %H:%M'))
    
    def test_should_display_data_hora_cadastro(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should display the corresponding date and time of registration

        :rtype: None
        """
        response = self.client.get(self.url)
        data_hora_cadastro = timezone.localtime(self.vaga.data_hora_cadastro).strftime('%d/%m/%Y %H:%M')
        self.assertContains(response, data_hora_cadastro)
    
    def test_should_have_link_to_company_website(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should have links to the corresponding website of the company

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertContains(response, f'href="{self.vaga.empresa_site}"')
    
    def test_should_have_link_to_new_registration(self) -> None:
        """
        GIVEN a homepage for the website

        WHEN I visit it

        THEN it should have a link to a page for registering new job opportunities

        :rtype: None
        """
        response = self.client.get(self.url)
        url = reverse('oportunidades_new')
        self.assertContains(response, f'href="{url}"')
    
    def test_should_have_link_to_detail_page(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should have a link to the corresponding detail page of that opportunity

        :rtype: None
        """
        response = self.client.get(self.url)
        url = reverse('oportunidades_detail', args=[str(self.vaga.pk)])
        self.assertContains(response, f'href="{url}"')            
    
    def test_should_have_link_to_edit_page(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should have a link to the corresponding edit page of that opportunity

        :rtype: None
        """
        response = self.client.get(self.url)
        url = reverse('oportunidades_edit', args=[str(self.vaga.pk)])
        self.assertContains(response, f'href="{url}"')
    
    def test_should_have_link_to_delete_page(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should have a link to the corresponding delete page of that opportunity

        :rtype: None
        """
        response = self.client.get(self.url)
        url = reverse('oportunidades_delete', args=[str(self.vaga.pk)])
        self.assertContains(response, f'href="{url}"')
    
    def test_should_not_display_empresa_endereco(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should not display the addresss of the company

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertNotContains(response, self.vaga.empresa_endereco)
    
    def test_should_not_display_empresa_email(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should not display the email of the company

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertNotContains(response, self.vaga.empresa_email)            
    
    def test_should_not_display_empresa_telefone_celular(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should not display the cellphone number of the company

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertNotContains(response, self.vaga.empresa_telefone_celular)

    def test_should_not_display_empresa_telefone_comercial(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should not display the landline number of the company

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertNotContains(response, self.vaga.empresa_telefone_comercial)
    
    def test_should_not_display_cargo_descricao(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should not display the job description

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertNotContains(response, self.vaga.cargo_descricao)

    def test_should_not_display_site_referencia(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should not display the website where the opportunity was found

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertNotContains(response, self.vaga.site_referencia)
    
    def test_should_display_situacao(self) -> None:
        """
        GIVEN a previously registered opportunity

        WHEN I visit the homepage

        THEN it should display the status of the opportunity

        :rtype: None
        """
        response = self.client.get(self.url)
        self.assertContains(response, self.vaga.situacao.label)
    
    def test_should_display_by_data_hora_cadastro_in_descending_order(self) -> None:
        """
        GIVEN registered opportunities

        WHEN I visit the homepage

        THEN it should display them by the date and time of registration in descending order

        :rtype: None
        """
        Vaga.objects.create(
            empresa_nome='Minha empresa 2',
            empresa_endereco='Meu endereço 2',
            empresa_email='empresa2@email.com',
            empresa_site='empresa2.com.br',
            empresa_telefone_celular='(11) 96712-0302',
            empresa_telefone_comercial='(11) 8067-2511',
            cargo_titulo='Cargo título 2',
            cargo_descricao='Cargo descrição 2',
            site_referencia='www.sitereferencia2.com.br',
            data_hora_entrevista=timezone.localtime(),
            situacao=Vaga.Status.WAITING,
        )
        Vaga.objects.create(
            empresa_nome='Minha empresa 3',
            empresa_endereco='Meu endereço 3',
            empresa_email='empresa3@email.com',
            empresa_site='empresa3.com.br',
            empresa_telefone_celular='(11) 96712-0302',
            empresa_telefone_comercial='(11) 8067-2511',
            cargo_titulo='Cargo título 3',
            cargo_descricao='Cargo descrição 3',
            site_referencia='www.sitereferencia3.com.br',
            data_hora_entrevista=timezone.localtime(),
            situacao=Vaga.Status.INTERVIEW_SCHEDULED,
        )
        response = self.client.get(self.url)
        vagas_from_page = list(response.context['vagas'])
        vagas_from_db = list(Vaga.objects.order_by('-data_hora_cadastro'))
        self.assertEqual(vagas_from_db, vagas_from_page)