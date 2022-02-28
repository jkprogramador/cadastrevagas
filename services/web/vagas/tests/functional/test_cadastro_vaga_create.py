from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from vagas.models import Vaga
from datetime import datetime as dt

class CadastroVagaCreateTest(TestCase):
    """
    As a user of the website

    I want to register job opportunities

    So that I can keep records of jobs I have applied for
    """

    def setUp(self) -> None:
        """
        GIVEN valid job opportunity data

        WHEN I submit the data to /oportunidades/new

        :rtype: None
        """
        self.data = {
            'empresa_nome': 'Minha empresa',
            'empresa_endereco': 'Meu endereço',
            'empresa_email': 'meuemail@email.com',
            'empresa_site': 'https://meusite.com.br',
            'empresa_telefone_celular': '(11) 98765-3201',
            'empresa_telefone_comercial': '(11) 8765-3201',
            'cargo_titulo': 'Título do cargo',
            'cargo_descricao': 'Descrição do cargo',
            'site_referencia': 'https://sitereferencia.com.br',
            'data_hora_entrevista': '07/04/2022 08:05',
        }

        self.response = self.client.post('/oportunidades/new', data=self.data, follow=True)
        self.vaga = Vaga.objects.get(empresa_nome=self.data['empresa_nome'])
    
    def test_should_create_job_opportunity(self) -> None:
        """
        THEN a job opportunity should be created

        :rtype: None
        """
        self.assertEqual(self.data['empresa_nome'], self.vaga.empresa_nome)
        self.assertEqual(self.data['empresa_endereco'], self.vaga.empresa_endereco)
        self.assertEqual(self.data['empresa_email'], self.vaga.empresa_email)
        self.assertEqual(self.data['empresa_site'], self.vaga.empresa_site)
        self.assertEqual(self.data['empresa_telefone_celular'], self.vaga.empresa_telefone_celular)
        self.assertEqual(self.data['empresa_telefone_comercial'], self.vaga.empresa_telefone_comercial)
        self.assertEqual(self.data['cargo_titulo'], self.vaga.cargo_titulo)
        self.assertEqual(self.data['cargo_descricao'], self.vaga.cargo_descricao)
        self.assertEqual(self.data['site_referencia'], self.vaga.site_referencia)
        data_hora_entrevista = timezone.make_aware(dt.strptime(self.data['data_hora_entrevista'], 
            "%d/%m/%Y %H:%M"))
        self.assertEqual(data_hora_entrevista, self.vaga.data_hora_entrevista)
    
    def test_should_redirect_to_detail_page(self) -> None:
        """
        THEN it should redirect to the detail page of the newly registered job opportunity

        :rtype: None
        """
        self.assertRedirects(self.response, 
            reverse('oportunidades_detail', args=[str(self.vaga.pk)]), 
            status_code=302, target_status_code=200
        )
    
    def test_should_show_success_message(self) -> None:
        """
        THEN it should show a success message confirming the creation of the job opportunity

        :rtype: None
        """
        self.assertContains(self.response, 'Vaga registrada com sucesso.')