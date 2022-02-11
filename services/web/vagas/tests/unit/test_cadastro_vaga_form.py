import unittest
from vagas.forms import CadastroVagasForm
from django.forms import CharField, EmailField, URLField, Textarea

class CadastroVagaFormTest(unittest.TestCase):
    """Test to ensure that the form for submitting job opportunities has the required fields."""

    def setUp(self) -> None:
        self.form = CadastroVagasForm()
        return super().setUp()
    
    def test_has_text_field_empresa_nome(self) -> None:
        """
        Ensure form has text field labeled "Nome da empresa".

        :return: None
        """
        field = self.form.fields['empresa_nome']
        self.assertIsInstance(field, CharField)
        self.assertEqual('Nome da empresa', field.label)
    
    def test_has_text_field_empresa_endereco(self) -> None:
        """
        Ensure form has text field labeled "Endereço da empresa".

        :return: None
        """
        field = self.form.fields['empresa_endereco']
        self.assertIsInstance(field, CharField)
        self.assertEqual('Endereço da empresa', field.label)

    def test_has_email_field_empresa_email(self) -> None:
        """
        Ensure form has email field labeled "Email da empresa".

        :return: None
        """
        field = self.form.fields['empresa_email']
        self.assertIsInstance(field, EmailField)
        self.assertEqual('Email da empresa', field.label)

    def test_has_url_field_empresa_site(self) -> None:
        """
        Ensure form has URL field labeled "Site da empresa".

        :return: None
        """
        field = self.form.fields['empresa_site']
        self.assertIsInstance(field, URLField)
        self.assertEqual('Site da empresa', field.label)

    def test_has_phone_field_empresa_telefone_celular(self) -> None:
        """
        Ensure form has phone field labeled "Telefone celular".

        :return: None
        """
        field = self.form.fields['empresa_telefone_celular']
        self.assertIsInstance(field, CharField)
        self.assertEqual('tel', field.widget.input_type)
        self.assertEqual('Telefone celular', field.label)

    def test_has_phone_field_empresa_telefone_comercial(self) -> None:
        """
        Ensure form has phone field labeled "Telefone comercial".

        :return: None
        """
        field = self.form.fields['empresa_telefone_comercial']
        self.assertIsInstance(field, CharField)
        self.assertEqual('tel', field.widget.input_type)
        self.assertEqual('Telefone comercial', field.label)

    def test_has_text_field_cargo_titulo(self) -> None:
        """
        Ensure form has text field labeled "Título do cargo".

        :return: None
        """
        field = self.form.fields['cargo_titulo']
        self.assertIsInstance(field, CharField)
        self.assertEqual('Título do cargo', field.label)

    def test_has_text_area_cargo_descricao(self) -> None:
        """
        Ensure form has text area labeled "Descrição do cargo".

        :return: None
        """
        field = self.form.fields['cargo_descricao']
        self.assertIsInstance(field, CharField)
        self.assertIsInstance(field.widget, Textarea)
        self.assertEqual('Descrição do cargo', field.label)

    def test_has_url_field_site_referencia(self) -> None:
        """
        Ensure form has URL field labeled "Site de referência".

        :return: None
        """
        field = self.form.fields['site_referencia']
        self.assertIsInstance(field, URLField)
        self.assertEqual('Site de referência', field.label)

    def test_has_datetime_field_data_hora_entrevista(self) -> None:
        """
        Ensure form has datetime field labeled "Entrevista em".

        :return: None
        """
        field = self.form.fields['data_hora_entrevista']
        self.assertIsInstance(field, CharField)
        self.assertEqual('datetime', field.widget.input_type)
        self.assertEqual('Entrevista em', field.label)