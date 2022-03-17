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

    def test_should_display_data_hora_entrevista_must_be_equal_to_or_later_than_current_datetime(self) -> None:
        """
        GIVEN a previously registered job opportunity with a blank datetime for the job interview

        WHEN I submit a datetime for the job interview prior to the current datetime

        THEN it should display an error message

        :rtype: None
        """
        vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_site='https://meusite.com.br',
            cargo_titulo='Título do cargo',
            site_referencia='https://sitereferencia.com.br',
        )
        data_hora_entrevista = timezone.localtime() - dt.timedelta(minutes=3)
        url = reverse('oportunidades_edit', args=[str(vaga.pk)])
        response = self.client.post(url, data={'data_hora_entrevista': data_hora_entrevista})
        self.assertContains(response, 'O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.')
    
    def test_should_allow_any_datetime_if_data_hora_entrevista_is_not_blank(self) -> None:
        """
        GIVEN a previously registered job opportunity with a datetime for the job interview

        WHEN I submit any datetime for the job interview

        THEN it should not display an error message

        :rtype: None
        """
        vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_site='https://meusite.com.br',
            cargo_titulo='Título do cargo',
            site_referencia='https://sitereferencia.com.br',
            data_hora_entrevista=timezone.localtime(),
        )
        url = reverse('oportunidades_edit', args=[str(vaga.pk)])
        data_hora_entrevista = timezone.localtime() - dt.timedelta(minutes=3)
        response = self.client.post(url, data={'data_hora_entrevista': data_hora_entrevista})
        self.assertNotContains(response, 'O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.')