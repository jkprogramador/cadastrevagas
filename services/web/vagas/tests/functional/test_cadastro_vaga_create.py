from django.test import TestCase
from django.utils import timezone
from vagas.models import Vaga
from datetime import datetime as dt
import re

class CadastroVagaCreateTest(TestCase):
    """
    As a user of the website

    I want to register job opportunities

    So that I can keep records of jobs I have applied for
    """

    def setUp(self) -> None:
        """
        GIVEN valid job opportunity data

        :return: None
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
            'data_hora_entrevista': '20/01/2022 15:30',
        }
        return super().setUp()
    
    def test_should_create_job_opportunity(self) -> None:
        """
        WHEN I submit the data to /oportunidades/new

        THEN a job opportunity should be created

        :return: None
        """
        self.client.post('/oportunidades/new', data=self.data)
        vaga = Vaga.objects.get(pk=1)
        self.assertEqual(self.data['empresa_nome'], vaga.empresa_nome)
        self.assertEqual(self.data['empresa_endereco'], vaga.empresa_endereco)
        self.assertEqual(self.data['empresa_email'], vaga.empresa_email)
        self.assertEqual(self.data['empresa_site'], vaga.empresa_site)
        tel_regex = re.compile('\D+')
        telefone_celular = tel_regex.sub('', self.data['empresa_telefone_celular'])
        self.assertEqual(telefone_celular, vaga.empresa_telefone_celular)
        telefone_comercial = tel_regex.sub('', self.data['empresa_telefone_comercial'])
        self.assertEqual(telefone_comercial, vaga.empresa_telefone_comercial)
        self.assertEqual(self.data['cargo_titulo'], vaga.cargo_titulo)
        self.assertEqual(self.data['cargo_descricao'], vaga.cargo_descricao)
        self.assertEqual(self.data['site_referencia'], vaga.site_referencia)
        data_hora_entrevista = timezone.make_aware(dt.strptime(self.data['data_hora_entrevista'], 
            "%d/%m/%Y %H:%M"))
        self.assertEqual(data_hora_entrevista, vaga.data_hora_entrevista)