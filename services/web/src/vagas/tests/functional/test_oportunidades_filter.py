from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from vagas.forms import OportunidadesFilterForm
from vagas.models import Vaga

class OportunidadesFilterTest(TestCase):
    """
    As a user of the website

    I want to filter job opportunities by some criteria

    So that I can see only the opportunities I want
    """

    def setUp(self) -> None:
        """
        GIVEN some previously registered opportunities and a page for filtering them

        :rtype: None
        """
        self.waiting = [
            Vaga.objects.create(
                empresa_nome='Minha empresa 1',
                empresa_endereco='Meu endereço 1',
                empresa_email='empresa1@email.com',
                empresa_site='empresa1.com.br',
                empresa_telefone_celular='(11) 96712-0302',
                empresa_telefone_comercial='(11) 8067-2511',
                cargo_titulo='Cargo título 1',
                cargo_descricao='Cargo descrição 1',
                site_referencia='www.sitereferencia1.com.br',
                data_hora_entrevista=timezone.localtime(),
                situacao=Vaga.Status.WAITING,
            ),
            Vaga.objects.create(
                empresa_nome='Minha empresa 4',
                empresa_endereco='Meu endereço 4',
                empresa_email='empresa4@email.com',
                empresa_site='empresa4.com.br',
                empresa_telefone_celular='(11) 96712-0302',
                empresa_telefone_comercial='(11) 8067-2511',
                cargo_titulo='Cargo título 4',
                cargo_descricao='Cargo descrição 4',
                site_referencia='www.sitereferencia4.com.br',
                data_hora_entrevista=timezone.localtime(),
                situacao=Vaga.Status.WAITING,
            )
        ]
        self.interview_scheduled = [
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
                situacao=Vaga.Status.INTERVIEW_SCHEDULED,
            ),
            Vaga.objects.create(
                empresa_nome='Minha empresa 5',
                empresa_endereco='Meu endereço 5',
                empresa_email='empresa5@email.com',
                empresa_site='empresa5.com.br',
                empresa_telefone_celular='(11) 96712-0302',
                empresa_telefone_comercial='(11) 8067-2511',
                cargo_titulo='Cargo título 5',
                cargo_descricao='Cargo descrição 5',
                site_referencia='www.sitereferencia5.com.br',
                data_hora_entrevista=timezone.localtime(),
                situacao=Vaga.Status.INTERVIEW_SCHEDULED,
            )
        ]
        self.rejected = [
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
                situacao=Vaga.Status.REJECTED,
            )
        ]

        self.url = reverse('homepage')
    
    def test_should_show_only_status_waiting(self) -> None:
        """
        WHEN I submit the filter with a value of Vaga.Status.WAITING for the status of the opportunity

        THEN only the opportunities with a value of Vaga.Status.WAITING for the status, ordered by datetime of registration in descending order, should be shown

        :rtype: None
        """
        response = self.client.get(f'{self.url}?situacao={Vaga.Status.WAITING}')
        vagas = list(response.context['vagas'])
        situacao_field = response.context['form'].fields['situacao']
        self.waiting.reverse()
        self.assertEqual(Vaga.Status.WAITING, situacao_field.initial)
        self.assertEqual(self.waiting, vagas)

    def test_should_show_only_status_interview_scheduled(self) -> None:
        """
        WHEN I submit the filter with a value of Vaga.Status.INTERVIEW_SCHEDULED for the status of the opportunity

        THEN only the opportunities with a value of Vaga.Status.INTERVIEW_SCHEDULED for the status, ordered by datetime of registration in descending order, should be shown

        :rtype: None
        """
        response = self.client.get(f'{self.url}?situacao={Vaga.Status.INTERVIEW_SCHEDULED}')
        vagas = list(response.context['vagas'])
        situacao_field = response.context['form'].fields['situacao']
        self.interview_scheduled.reverse()
        self.assertEqual(Vaga.Status.INTERVIEW_SCHEDULED, situacao_field.initial)
        self.assertEqual(self.interview_scheduled, vagas)

    def test_should_show_only_status_rejected(self) -> None:
        """
        WHEN I submit the filter with a value of Vaga.Status.REJECTED for the status of the opportunity

        THEN only the opportunities with a value of Vaga.Status.REJECTED for the status, ordered by datetime of registration in descending order, should be shown

        :rtype: None
        """
        response = self.client.get(f'{self.url}?situacao={Vaga.Status.REJECTED}')
        situacao_field = response.context['form'].fields['situacao']
        vagas = list(response.context['vagas'])
        self.rejected.reverse()
        self.assertEqual(Vaga.Status.REJECTED, situacao_field.initial)
        self.assertEqual(self.rejected, vagas)
    
    def test_should_show_all(self) -> None:
        """
        WHEN I submit the filter with a choice of 'Todas' for the status of the opportunity

        THEN all opportunities, ordered by datetime of registration in descending order, should be shown

        :rtype: None
        """
        response = self.client.get(f'{self.url}?situacao=')
        actual = list(response.context['vagas'])
        situacao_field = response.context['form'].fields['situacao']
        expected = list(Vaga.objects.order_by('-data_hora_cadastro'))
        self.assertEqual((None, 'Todas',), situacao_field.initial)
        self.assertEqual(expected, actual)
    
    def test_should_show_by_oldest_data_hora_cadastro(self) -> None:
        """
        WHEN I submit the filter with a value of 'Mais antigas' for the order of the datetime of registration

        THEN the opportunities ordered by oldest datetime of registration should be shown

        :rtype: None
        """
        response = self.client.get(f'{self.url}?data_hora_cadastro_order={OportunidadesFilterForm.DataHoraCadastroOrder.OLDEST}')
        data_hora_cadastro_order = response.context['form'].fields['data_hora_cadastro_order']
        expected = list(Vaga.objects.order_by('data_hora_cadastro'))
        actual = list(response.context['vagas'])
        self.assertEqual(OportunidadesFilterForm.DataHoraCadastroOrder.OLDEST, data_hora_cadastro_order.initial)
        self.assertEqual(expected, actual)

    def test_should_show_by_newest_data_hora_cadastro(self) -> None:
        """
        WHEN I submit the filter with a value of 'Mais recentes' for the order of the datetime of registration

        THEN the opportunities ordered by newest datetime of registration should be shown

        :rtype: None
        """
        response = self.client.get(f'{self.url}?data_hora_cadastro_order={OportunidadesFilterForm.DataHoraCadastroOrder.NEWEST}')
        data_hora_cadastro_order = response.context['form'].fields['data_hora_cadastro_order']
        expected = list(Vaga.objects.order_by('-data_hora_cadastro'))
        actual = list(response.context['vagas'])
        self.assertEqual(OportunidadesFilterForm.DataHoraCadastroOrder.NEWEST, data_hora_cadastro_order.initial)
        self.assertEqual(expected, actual)