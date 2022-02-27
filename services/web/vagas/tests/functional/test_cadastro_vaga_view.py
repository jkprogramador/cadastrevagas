from django.test import SimpleTestCase
from django.forms import CharField, EmailField, URLField, Textarea

class CadastroVagaViewTest(SimpleTestCase):
    """
    As a user of the website

    I want a page with a form

    So that a I can submit new job opportunities
    """

    def setUp(self) -> None:
        """
        GIVEN a page at /oportunidades/new

        WHEN I access the form on this page

        :rtype: None
        """
        self.response = self.client.get('/oportunidades/new')
        self.form = self.response.context['form']
    
    def test_should_have_text_field_for_nome_da_empresa(self) -> None:
        """
        THEN it should have a text field for the company's name

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_nome'], CharField)
    
    def test_should_have_text_field_for_endereco_da_empresa(self) -> None:
        """
        THEN it should have a text field for the company's address

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_endereco'], CharField)

    def test_should_have_email_field_for_email_da_empresa(self) -> None:
        """
        THEN it should have an email field for the company's email address

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_email'], EmailField)

    def test_should_have_url_field_for_site_da_empresa(self) -> None:
        """
        THEN it should have a URL field for the company's website

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_site'], URLField)

    def test_should_have_text_field_for_telefone_celular_da_empresa(self) -> None:
        """
        THEN it should have a text field for the company's mobile phone

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_telefone_celular'], CharField)

    def test_should_have_phone_field_for_telefone_comercial_da_empresa(self) -> None:
        """
        THEN it should have a phone field for the company's landline

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_telefone_comercial'], CharField)

    def test_should_have_text_field_for_titulo_do_cargo(self) -> None:
        """
        THEN it should have a text field for the job title

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['cargo_titulo'], CharField)

    def test_should_have_text_area_for_descricao_do_cargo(self) -> None:
        """
        THEN it should have a text area for the job description

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['cargo_descricao'].widget, Textarea)

    def test_should_have_url_field_for_site_de_referencia(self) -> None:
        """
        THEN it should have a URL field determining where the opportunity was found

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['site_referencia'], URLField)

    def test_should_have_datetime_field_for_data_e_hora_da_entrevista(self) -> None:
        """
        THEN it should have a datetime field for the date and time of a job interview

        :rtype: None
        """
        self.assertEqual('datetime', 
            self.form.fields['data_hora_entrevista'].widget.input_type)
    
    def test_should_have_button_to_submit_form(self) -> None:
        """
        THEN it should have a button labeled "Cadastrar" to submit the form.

        :rtype: None
        """
        self.assertContains(self.response, 'Cadastrar')
        self.assertContains(self.response, 'type=submit')