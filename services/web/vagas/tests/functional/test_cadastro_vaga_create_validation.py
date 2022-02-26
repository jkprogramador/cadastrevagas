from django.test import SimpleTestCase
from django.urls import reverse

class CadastroVagaCreateValidationTest(SimpleTestCase):
    """
    As a user of the website

    I want to be informed of any errors when registering a job opportunity

    So that I can submit valid data only
    """
    
    def setUp(self) -> None:
        """
        GIVEN an existing page for registering job opportunities

        :rtype: None
        """
        self.url = reverse('oportunidades_new')
    
    def test_should_display_empresa_nome_is_required(self) -> None:
        """
        WHEN I submit an empty value for the company's name

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={'empresa_nome': ''})
        self.assertContains(response, 'O campo Nome da empresa é obrigatório.')
    
    def test_should_display_empresa_nome_cannot_exceed_maximum_length(self) -> None:
        """
        WHEN I submit a value for the company's name that exceeds a certain length

        THEN it should display an error message

        :rtype: None
        """
        empresa_nome = 'X' * 101
        response = self.client.post(self.url, data={'empresa_nome': empresa_nome})
        self.assertContains(response, 'O campo Nome da empresa pode conter no máximo 100 caracteres.')
    
    def test_should_display_empresa_endereco_cannot_exceed_maximum_length(self) -> None:
        """
        WHEN I submit a value for the company's address that exceeds a certain length

        THEN it should display an error message

        :rtype: None
        """
        empresa_endereco = 'X' * 201
        response = self.client.post(self.url, data={'empresa_endereco': empresa_endereco})
        self.assertContains(response, 'O campo Endereço da empresa pode conter no máximo 200 caracteres.')
    
    def test_should_display_empresa_email_must_be_valid_email(self) -> None:
        """
        WHEN I submit an invalid email for the company's email

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={'empresa_email': 'foo@'})
        self.assertContains(response, 'O campo Email da empresa deve conter um email válido.')
    
    def test_should_display_empresa_site_is_required(self) -> None:
        """
        WHEN I submit an empty value for the company's website

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={'empresa_site': ''})
        self.assertContains(response, 'O campo Site da empresa é obrigatório.')
    
    def test_should_display_empresa_site_must_be_valid_url(self) -> None:
        """
        WHEN I submit an invalid URL for the company's website

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={'empresa_site': 'foo.'})
        self.assertContains(response, 'O campo Site da empresa deve conter um endereço web válido.')
    
    def test_should_display_empresa_telefone_celular_must_be_valid_cellphone(self) -> None:
        """
        WHEN I submit an invalid cellphone/cellphone in an incorrect format for the company's cellphone

        THEN it should display an error message

        :rtype: None
        """
        expected_error_message = 'O campo Telefone celular da empresa deve conter um número válido. Ex.: (DDD) 99999-9999'
        response = self.client.post(self.url, data={'empresa_telefone_celular': '(11) 8451-6302'})
        self.assertContains(response, expected_error_message)

        response = self.client.post(self.url, data={'empresa_telefone_celular': '11978032511'})
        self.assertContains(response, expected_error_message)
    
    def test_should_display_empresa_telefone_comercial_must_be_valid_landline(self) -> None:
        """
        WHEN I submit an invalid landline number/landline number in an incorrect format for the company's landline

        THEN it should display an error message

        :rtype: None
        """
        expected_error_message = 'O campo Telefone comercial da empresa deve conter um número válido. Ex.: (DDD) 9999-9999'
        response = self.client.post(self.url, data={'empresa_telefone_comercial': '(11) 94539-0485'})
        self.assertContains(response, expected_error_message)

        response = self.client.post(self.url, data={'empresa_telefone_comercial': '1184752517'})
        self.assertContains(response, expected_error_message)
    
    def test_should_display_cargo_titulo_is_required(self) -> None:
        """
        WHEN I submit an empty value for the job title

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={'cargo_titulo': ''})
        self.assertContains(response, 'O campo Título do cargo é obrigatório.')
    
    def test_should_display_cargo_titulo_cannot_exceed_maximum_length(self) -> None:
        """
        WHEN I submit a value for the job title that exceeds its maximum length

        THEN it should display an error message

        :rtype: None
        """
        cargo_titulo = 'X' * 51
        response = self.client.post(self.url, data={'cargo_titulo': cargo_titulo})
        self.assertContains(response, 'O campo Título do cargo pode conter no máximo 50 caracteres.')
    
    def test_should_display_site_referencia_is_required(self) -> None:
        """
        WHEN I submit an empty value for the reference website where the opportunity was found

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={'site_referencia': ''})
        self.assertContains(response, 'O campo Site de referência é obrigatório.')
    
    def test_should_display_site_referencia_must_be_valid_url(self) -> None:
        """
        WHEN I submit an invalid URL for the reference website where the opportunity was found

        THEN it should display an error message

        :rtype: None
        """
        response = self.client.post(self.url, data={'site_referencia': 'foo.'})
        self.assertContains(response, 'O campo Site de referência deve conter um endereço web válido.')
    
    def test_should_display_data_hora_entrevista_must_be_valid_date_and_time(self) -> None:
        """
        WHEN I submit an invalid datetime/datetime in an incorrect format for the date and time of a interview

        THEN it should display an error message

        :rtype: None
        """
        expected_error_message = 'O campo Data e hora da entrevista deve conter uma data e horário válidos. Ex.: dd/mm/YYYY HH:ii'
        response = self.client.post(self.url, data={'data_hora_entrevista': '32/02/2022 09:03'})
        self.assertContains(response, expected_error_message)

        response = self.client.post(self.url, data={'data_hora_entrevista': '2022 10 23 08:07'})
        self.assertContains(response, expected_error_message)