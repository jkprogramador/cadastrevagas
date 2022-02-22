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
        """
        GIVEN previously registered job opportunities

        WHEN I go to the homepage

        :rtype: None
        """
        self.data = [
            {
                'empresa_nome': 'Minha empresa 1',
                'empresa_endereco': 'Meu endereço 1',
                'empresa_email': 'empresa1@email.com',
                'empresa_site': 'empresa1.com.br',
                'empresa_telefone_celular': '(11) 96712-0302',
                'empresa_telefone_comercial': '(11) 8067-2511',
                'cargo_titulo': 'Cargo título 1',
                'cargo_descricao': 'Cargo descrição 1',
                'site_referencia': 'www.sitereferencia1.com.br',
                'data_hora_entrevista': '04/07/2022 08:01',
            },
            {
                'empresa_nome': 'Minha empresa 2',
                'empresa_endereco': 'Meu endereço 2',
                'empresa_email': 'empresa2@email.com',
                'empresa_site': 'empresa2.com.br',
                'empresa_telefone_celular': '(11) 95536-4659',
                'empresa_telefone_comercial': '(11) 7541-0606',
                'cargo_titulo': 'Cargo título 2',
                'cargo_descricao': 'Cargo descrição 2',
                'site_referencia': 'https://www.sitereferencia2.com.br',
                'data_hora_entrevista': '03/04/2022 09:54',
            },
            {
                'empresa_nome': 'Minha empresa 3',
                'empresa_endereco': 'Meu endereço 3',
                'empresa_email': 'empresa3@email.com',
                'empresa_site': 'empresa3.com.br',
                'empresa_telefone_celular': '(11) 90785-9251',
                'empresa_telefone_comercial': '(11) 6441-2507',
                'cargo_titulo': 'Cargo título 3',
                'cargo_descricao': 'Cargo descrição 3',
                'site_referencia': 'http://sitereferencia3.com.br',
                'data_hora_entrevista': '19/10/2022 15:43',
            },
        ]

        for data in self.data:
            Vaga.objects.create(
                empresa_nome=data['empresa_nome'],
                empresa_endereco=data['empresa_endereco'],
                empresa_email=data['empresa_email'],
                empresa_site=data['empresa_site'],
                empresa_telefone_celular=data['empresa_telefone_celular'],
                empresa_telefone_comercial=data['empresa_telefone_comercial'],
                cargo_titulo=data['cargo_titulo'],
                cargo_descricao=data['cargo_descricao'],
                site_referencia=data['site_referencia'],
                data_hora_entrevista=data['data_hora_entrevista']
            )
        
        self.response = self.client.get('/')
    
    def test_should_have_link_to_homepage(self) -> None:
        """
        THEN it should have a link to the homepage

        :rtype: None
        """
        url = reverse('homepage')
        self.assertContains(self.response, f'href="{url}"')
    
    def test_should_display_cargo_titulo(self) -> None:
        """
        THEN it should display the corresponding job titles for registered job opportunities

        :rtype: None
        """
        for data in self.data:
            self.assertContains(self.response, data['cargo_titulo'])
    
    def test_should_display_empresa_nome(self) -> None:
        """
        THEN it should display the corresponding companies' names for registered job opportunities

        :rtype: None
        """
        for data in self.data:
            self.assertContains(self.response, data['empresa_nome'])
    
    def test_should_display_data_hora_entrevista(self) -> None:
        """
        THEN it should display the corresponding date and time of each job interviews

        :rtype: None
        """
        for data in self.data:
            self.assertContains(self.response, data['data_hora_entrevista'])
    
    def test_should_display_data_hora_cadastro(self) -> None:
        """
        THEN it should display the corresponding date and time of each registration

        :rtype: None
        """
        for data in self.data:
            vaga = Vaga.objects.get(empresa_nome=data['empresa_nome'])
            local_data_hora_cadastro = timezone.localtime(vaga.data_hora_cadastro)
            formatted_data_hora_cadastro = local_data_hora_cadastro.strftime('%d/%m/%Y %H:%M')
            self.assertContains(self.response, formatted_data_hora_cadastro)
    
    def test_should_have_link_to_each_company_website(self) -> None:
        """
        THEN it should have links to the corresponding companies' websites

        :rtype: None
        """
        for data in self.data:
            url = data['empresa_site']
            self.assertContains(self.response, f'href="{url}"')
    
    def test_should_have_link_to_register_new_opportunities(self) -> None:
        """
        THEN it should have a link to a page for registering new job opportunities

        :rtype: None
        """
        url = reverse('oportunidades_new')
        self.assertContains(self.response, f'href="{url}"')
    
    def test_should_have_link_to_each_detail_page(self) -> None:
        """
        THEN each job opportunity should have a link to its corresponding detail page

        :rtype: None
        """
        for data in self.data:
            vaga = Vaga.objects.get(empresa_nome=data['empresa_nome'])
            url = reverse('oportunidades_detail', args=[str(vaga.pk)])
            self.assertContains(self.response, f'href="{url}"')
    
    def test_should_have_link_to_edit_job_opportunity(self) -> None:
        """
        THEN each job opportunity should have a link to edit its corresponding data

        :rtype: None
        """
        for data in self.data:
            vaga = Vaga.objects.get(empresa_nome=data['empresa_nome'])
            url = reverse('oportunidades_edit', args=[str(vaga.pk)])
            self.assertContains(self.response, f'href="{url}"')
    
    def test_should_have_link_to_delete_job_opportunity(self) -> None:
        """
        THEN each job opportunity should have a link to delete its entry

        :rtype: None
        """
        for data in self.data:
            vaga = Vaga.objects.get(empresa_nome=data['empresa_nome'])
            url = reverse('oportunidades_delete', args=[str(vaga.pk)])
            self.assertContains(self.response, f'href="{url}"')
    
    def test_should_not_display_empresa_endereco(self) -> None:
        """
        THEN it should not display the companies' addresses

        :rtype: None
        """
        for data in self.data:
            self.assertNotContains(self.response, data['empresa_endereco'])
    
    def test_should_not_display_empresa_email(self) -> None:
        """
        THEN it should not display the companies' emails

        :rtype: None
        """
        for data in self.data:
            self.assertNotContains(self.response, data['empresa_email'])
    
    def test_should_not_display_empresa_telefone_celular(self) -> None:
        """
        THEN it should not display the companies' cellphone numbers

        :rtype: None
        """
        for data in self.data:
            self.assertNotContains(self.response, data['empresa_telefone_celular'])

    def test_should_not_display_empresa_telefone_comercial(self) -> None:
        """
        THEN it should not display the companies' landline numbers

        :rtype: None
        """
        for data in self.data:
            self.assertNotContains(self.response, data['empresa_telefone_comercial'])
    
    def test_should_not_display_cargo_descricao(self) -> None:
        """
        THEN it should not display the job descriptions

        :rtype: None
        """
        for data in self.data:
            self.assertNotContains(self.response, data['cargo_descricao'])

    def test_should_not_display_site_referencia(self) -> None:
        """
        THEN it should not display the websites where the opportunities were found

        :rtype: None
        """
        for data in self.data:
            self.assertNotContains(self.response, data['site_referencia'])