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

        :return: None
        """
        self.response = self.client.get('/oportunidades/new')
        self.form = self.response.context['form']
        return super().setUp()
    
    def test_should_have_text_field_for_nome_da_empresa(self) -> None:
        """
        THEN it should have a text field labeled "Nome da empresa"

        :return: None
        """
        field = self.form.fields['empresa_nome']
        self.assertIsInstance(field, CharField)
        self.assertEqual('Nome da empresa', field.label)
    
    def test_should_have_text_field_for_endereco_da_empresa(self) -> None:
        """
        THEN it should have a text field labeled "Endereço da empresa"

        :return: None
        """
        field = self.form.fields['empresa_endereco']
        self.assertIsInstance(field, CharField)
        self.assertEqual('Endereço da empresa', field.label)

    def test_should_have_email_field_for_email_da_empresa(self) -> None:
        """
        THEN it should have an email field labeled "Email da empresa"

        :return: None
        """
        field = self.form.fields['empresa_email']
        self.assertIsInstance(field, EmailField)
        self.assertEqual('Email da empresa', field.label)

    def test_should_have_url_field_for_site_da_empresa(self) -> None:
        """
        THEN it should have a URL field labeled "Site da empresa"

        :return: None
        """
        field = self.form.fields['empresa_site']
        self.assertIsInstance(field, URLField)
        self.assertEqual('Site da empresa', field.label)

    def test_should_have_phone_field_for_telefone_celular_da_empresa(self) -> None:
        """
        THEN it should have a phone field labeled "Telefone celular"

        :return: None
        """
        field = self.form.fields['empresa_telefone_celular']
        self.assertEqual('tel', field.widget.input_type)
        self.assertEqual('Telefone celular', field.label)

    def test_should_have_phone_field_for_telefone_comercial_da_empresa(self) -> None:
        """
        THEN it should have a phone field labeled "Telefone comercial"

        :return: None
        """
        field = self.form.fields['empresa_telefone_comercial']
        self.assertEqual('tel', field.widget.input_type)
        self.assertEqual('Telefone comercial', field.label)

    def test_should_have_text_field_for_titulo_do_cargo(self) -> None:
        """
        THEN it should have a text field labeled "Título do cargo"

        :return: None
        """
        field = self.form.fields['cargo_titulo']
        self.assertEqual('Título do cargo', field.label)

    def test_should_have_text_area_for_descricao_do_cargo(self) -> None:
        """
        THEN it should have a text area labeled "Descrição do cargo"

        :return: None
        """
        field = self.form.fields['cargo_descricao']
        self.assertIsInstance(field.widget, Textarea)
        self.assertEqual('Descrição do cargo', field.label)

    def test_should_have_url_field_for_site_de_referencia(self) -> None:
        """
        THEN it should have a URL field labeled "Site de referência"

        :return: None
        """
        field = self.form.fields['site_referencia']
        self.assertIsInstance(field, URLField)
        self.assertEqual('Site de referência', field.label)

    def test_should_have_datetime_field_for_data_e_hora_da_entrevista(self) -> None:
        """
        THEN it should have a datetime field labeled "Entrevista em"

        :return: None
        """
        field = self.form.fields['data_hora_entrevista']
        self.assertIsInstance(field, CharField)
        self.assertEqual('datetime', field.widget.input_type)
        self.assertEqual('Entrevista em', field.label)
    
    def test_should_have_button_to_submit_form(self) -> None:
        """
        THEN it should have a button labeled "Cadastrar" to submit the form.

        :return: None
        """
        self.assertContains(self.response, 'Cadastrar')
        self.assertContains(self.response, 'type=submit')