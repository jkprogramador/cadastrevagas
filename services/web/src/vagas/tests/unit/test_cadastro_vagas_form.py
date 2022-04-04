import unittest
from vagas.forms import CadastroVagasForm
from vagas.models import Vaga
from django.forms import (
    CharField,
    EmailField,
    URLField,
    Textarea,
    DateTimeField,
    ChoiceField,
)

class CadastroVagasFormTest(unittest.TestCase):
    """Test to ensure that the form for submitting job opportunities has the required fields."""

    def setUp(self) -> None:
        self.form = CadastroVagasForm()
    
    def test_has_text_field_empresa_nome(self) -> None:
        """
        Ensure form has text field for the company's name.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_nome'], CharField)
    
    def test_has_text_field_empresa_endereco(self) -> None:
        """
        Ensure form has text field for the company's address.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_endereco'], CharField)

    def test_has_email_field_empresa_email(self) -> None:
        """
        Ensure form has email field for the company's email address.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_email'], EmailField)

    def test_has_url_field_empresa_site(self) -> None:
        """
        Ensure form has URL field for the company's website.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_site'], URLField)

    def test_has_phone_field_empresa_telefone_celular(self) -> None:
        """
        Ensure form has phone field for the company's cellphone.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_telefone_celular'], CharField)

    def test_has_phone_field_empresa_telefone_comercial(self) -> None:
        """
        Ensure form has phone field for the company's landline.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['empresa_telefone_comercial'], CharField)

    def test_has_text_field_cargo_titulo(self) -> None:
        """
        Ensure form has text field for the job title.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['cargo_titulo'], CharField)

    def test_has_text_area_cargo_descricao(self) -> None:
        """
        Ensure form has text area for the job description.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['cargo_descricao'].widget, Textarea)

    def test_has_url_field_site_referencia(self) -> None:
        """
        Ensure form has URL field for the website where the opportunity was found.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['site_referencia'], URLField)

    def test_has_datetime_field_data_hora_entrevista(self) -> None:
        """
        Ensure form has datetime field for the date and time of a job interview.

        :rtype: None
        """
        self.assertIsInstance(self.form.fields['data_hora_entrevista'], DateTimeField)
    
    def test_does_not_have_data_e_hora_cadastro_field(self) -> None:
        """
        Ensure form does not have field for the date and time of registration.

        :rtype: None
        """
        with self.assertRaises(KeyError):
            self.form.fields['data_hora_cadastro']
    
    def test_does_not_have_data_e_hora_atualizacao_field(self) -> None:
        """
        Ensure form does not have field for the date and time of the last update.

        :rtype: None
        """
        with self.assertRaises(KeyError):
            self.form.fields['data_hora_atualizacao']
    
    def test_has_choice_field_situacao(self) -> None:
        """
        Ensure form has choice field for selecting the status of a job opportunity.

        :rtype: None
        """
        field = self.form.fields['situacao']
        self.assertIsInstance(field, ChoiceField)
        self.assertIn(('W', 'Aguardando retorno',), field.choices)
        self.assertIn(('S', 'Entrevista agendada',), field.choices)
        self.assertIn(('R', 'Rejeitado',), field.choices)
        self.assertEqual(Vaga.Status.WAITING, field.initial)