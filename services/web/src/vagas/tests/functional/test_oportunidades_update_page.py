from django.test import TestCase
from django.utils import timezone
from django.forms import (
    CharField,
    EmailField,
    URLField,
    Textarea,
    DateTimeField,
    ChoiceField,
)
from vagas.models import Vaga

class CadastroVagaEditViewTest(TestCase):
    """
    As a user of the website

    I want a page with a form

    So that I can edit details of a job opportunity I've registered
    """

    def setUp(self) -> None:
        """
        GIVEN a previously registered job opportunity

        WHEN I go to /oportunidades/<ID of job opportunity>/edit

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
            situacao=Vaga.Status.INTERVIEW_SCHEDULED,
        )

        self.response = self.client.get(f'/oportunidades/{str(self.vaga.pk)}/edit')
        self.form = self.response.context['form']
    
    def test_should_have_text_field_filled_with_nome_da_empresa(self) -> None:
        """
        THEN it should have a text field filled with the corresponding company's name

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_nome'], CharField)
        self.assertEqual(self.vaga.empresa_nome, self.form.initial['empresa_nome'])
    
    def test_should_have_text_field_filled_with_endereco_da_empresa(self) -> None:
        """
        THEN it should have a text field filled with the corresponding company's address

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_endereco'], CharField)
        self.assertEqual(self.vaga.empresa_endereco, self.form.initial['empresa_endereco'])
    
    def test_should_have_email_field_filled_with_email_da_empresa(self) -> None:
        """
        THEN it should have an email field filled with the corresponding company's email

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_email'], EmailField)
        self.assertEqual(self.vaga.empresa_email, self.form.initial['empresa_email'])
    
    def test_should_have_url_field_filled_with_site_da_empresa(self) -> None:
        """
        THEN it should have a URL field filled with the corresponding company's website URL

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_site'], URLField)
        self.assertEqual(self.vaga.empresa_site, self.form.initial['empresa_site'])
    
    def test_should_have_phone_field_filled_with_telefone_celular_da_empresa(self) -> None:
        """
        THEN it should have a phone field filled with the corresponding company's cellphone in the correct format

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_telefone_celular'], CharField)
        self.assertEqual(self.vaga.empresa_telefone_celular, self.form.initial['empresa_telefone_celular'])
    
    def test_should_have_phone_field_filled_with_telefone_comercial_da_empresa(self) -> None:
        """
        THEN it should have a phone field filled with the corresponding company's landline in the correct format

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_telefone_comercial'], CharField)
        self.assertEqual(self.vaga.empresa_telefone_comercial, self.form.initial['empresa_telefone_comercial'])
    
    def test_should_have_text_field_filled_with_titulo_do_cargo(self) -> None:
        """
        THEN it should have a text field filled with the corresponding job title

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['cargo_titulo'], CharField)
        self.assertEqual(self.vaga.cargo_titulo, self.form.initial['cargo_titulo'])
    
    def test_should_have_text_area_filled_with_descricao_do_cargo(self) -> None:
        """
        THEN it should have a text area filled with the corresponding job description

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['cargo_descricao'].widget, Textarea)
        self.assertEqual(self.vaga.cargo_descricao, self.form.initial['cargo_descricao'])
    
    def test_should_have_url_field_filled_with_site_referencia(self) -> None:
        """
        THEN it should have a URL field filled with the corresponding website where the opportunity was found

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['site_referencia'], URLField)
        self.assertEqual(self.vaga.site_referencia, self.form.initial['site_referencia'])
    
    def test_should_have_datetime_field_filled_with_data_e_hora_da_entrevista(self) -> None:
        """
        THEN it should have a datetime field filled with the corresponding date and time of the job interview

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['data_hora_entrevista'], DateTimeField)
        local_datetime = self.vaga.data_hora_entrevista.strftime('%d/%m/%Y %H:%M')
        self.assertEqual(local_datetime, self.form.initial['data_hora_entrevista'])
    
    def test_should_have_choice_field_with_situacao(self) -> None:
        """
        THEN it should have a choice field with the corresponding status of the job interview selected as default

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['situacao'], ChoiceField)
        self.assertEqual(self.vaga.situacao, self.form.initial['situacao'])
    
    def test_should_have_a_button_to_submit_the_form(self) -> None:
        """
        THEN it should have a button to submit the form

        :rtype: None
        """
        self.assertContains(self.response, 'type=submit')