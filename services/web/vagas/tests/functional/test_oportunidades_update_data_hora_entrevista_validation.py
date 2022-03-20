from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime as dt
from vagas.models import Vaga

class CadastroVagaUpdateDataHoraEntrevistaValidationTest(TestCase):
    """
    As a user of the website

    I want to be informed of any errors when updating the datetime of a job interview

    So that I can submit valid data only
    """

    def setUp(self) -> None:
        """
        GIVEN a previously registered opportunity

        :rtype: None
        """
        self.vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_site='https://meusite.com.br',
            cargo_titulo='Título do cargo',
            site_referencia='https://sitereferencia.com.br',
            data_hora_entrevista=timezone.localtime(),
        )
        self.url = reverse('oportunidades_edit', args=[str(self.vaga.pk)])

    def test_must_be_blank_if_situacao_is_waiting(self) -> None:
        """
        WHEN I submit the status of the opportunity with a value of Vaga.Status.WAITING and a value for the date and time of interview

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={
            'situacao': Vaga.Status.WAITING,
            'data_hora_entrevista': timezone.localtime().strftime('%d/%m/%Y %H:%M'),
        })
        self.assertContains(response,
            "O campo Data e horário da entrevista deve estar vazio caso a situação do cadastro seja 'Aguardando retorno'."
        )

    def test_cannot_be_blank_if_situacao_is_interview_scheduled(self) -> None:
        """
        WHEN I submit the status of the opportunity with a value of Vaga.Status.INTERVIEW_SCHEDULED and a blank value for the date and time of interview

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={
            'situacao': Vaga.Status.INTERVIEW_SCHEDULED,
            'data_hora_entrevista': '',
        })
        self.assertContains(response,
            "O campo Data e o horário da entrevista deve ser preenchido caso a situação do cadastro seja 'Entrevista agendada'."
        )

    def test_must_be_equal_to_or_later_than_current_datetime_if_situacao_is_interview_scheduled(self) -> None:
        """
        WHEN I submit the status of the opportunity with a value of Vaga.Status.INTERVIEW_SCHEDULED and a datetime for the interview prior to the current datetime

        THEN it should display an error message

        :rtype: None
        """
        data_hora_entrevista = timezone.localtime() - dt.timedelta(minutes=3)
        response = self.client.post(self.url, data={
            'situacao': Vaga.Status.INTERVIEW_SCHEDULED,
            'data_hora_entrevista': data_hora_entrevista,
        })
        self.assertContains(response, 'O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.')