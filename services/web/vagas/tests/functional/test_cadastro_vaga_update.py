from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from datetime import datetime as dt
from vagas.models import Vaga

class CadastroVagaUpdateTest(TestCase):
    """
    As a user of the website

    I want to update details of a job opportunity

    So that I have the most up-to-date information
    """

    def setUp(self) -> None:
        """
        GIVEN a previously registered job opportunity

        WHEN I submit new data to /oportunidades/<ID of job opportunity>/edit

        :rtype: None
        """
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
            data_hora_entrevista=timezone.localtime(),
        )

        self.new_data = {
            'empresa_nome': 'Nossa empresa',
            'empresa_endereco': 'Nosso endereço',
            'empresa_email': 'nossoemail@email.com',
            'empresa_site': 'https://nossosite.com.br',
            'empresa_telefone_celular': '(11) 92314-6907',
            'empresa_telefone_comercial': '(11) 5478-0011',
            'cargo_titulo': 'Título da posição',
            'cargo_descricao': 'Descrição da posição',
            'site_referencia': 'https://nossositereferencia.com.br',
            'data_hora_entrevista': '19/07/2022 16:38',
        }

        self.response = self.client.post(f'/oportunidades/{str(self.vaga.pk)}/edit', 
            data=self.new_data, follow=True)
    
    def test_should_update_job_opportunity(self) -> None:
        """
        THEN the existing job opportunity should be updated with the new data

        :rtype: None
        """
        vaga = Vaga.objects.get(pk=self.vaga.pk)
        self.assertEqual(self.new_data['empresa_nome'], vaga.empresa_nome)
        self.assertEqual(self.new_data['empresa_endereco'], vaga.empresa_endereco)
        self.assertEqual(self.new_data['empresa_email'], vaga.empresa_email)
        self.assertEqual(self.new_data['empresa_site'], vaga.empresa_site)
        self.assertEqual(self.new_data['empresa_telefone_celular'], vaga.empresa_telefone_celular)
        self.assertEqual(self.new_data['empresa_telefone_comercial'], vaga.empresa_telefone_comercial)
        self.assertEqual(self.new_data['cargo_titulo'], vaga.cargo_titulo)
        self.assertEqual(self.new_data['cargo_descricao'], vaga.cargo_descricao)
        self.assertEqual(self.new_data['site_referencia'], vaga.site_referencia)
        data_hora_entrevista = timezone.make_aware(dt.strptime(self.new_data['data_hora_entrevista'], 
            "%d/%m/%Y %H:%M"))
        self.assertEqual(data_hora_entrevista, vaga.data_hora_entrevista)
    
    def test_should_redirect_to_detail_page(self) -> None:
        """
        THEN it should redirect to the detail page of the job opportunity

        :rtype: None
        """
        self.assertRedirects(self.response, 
            reverse('oportunidades_detail', args=[str(self.vaga.pk)]), 
            status_code=302, target_status_code=200
        )
    
    def test_should_show_success_message(self) -> None:
        """
        THEN it should show a success message confirming the update of the job opportunity

        :rtype: None
        """
        self.assertContains(self.response, 'Vaga atualizada com sucesso.')