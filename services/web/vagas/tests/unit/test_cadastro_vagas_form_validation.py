from django.test import SimpleTestCase
from vagas.forms import CadastroVagasForm

class CadastroVagasFormValidationTest(SimpleTestCase):
    """Ensure CadastroVagasForm performs the necessary validation."""
    
    def test_empresa_nome_is_required(self) -> None:
        """
        Ensure that empresa_nome is required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_nome': ''})
        self.assertIn('O campo Nome da empresa é obrigatório.', form.errors['empresa_nome'])
    
    def test_empresa_endereco_is_not_required(self) -> None:
        """
        Ensure that empresa_endereco is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_endereco': ''})
        self.assertNotIn('empresa_endereco', form.errors)
    
    def test_empresa_email_is_not_required(self) -> None:
        """
        Ensure that empresa_email is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_email': ''})
        self.assertNotIn('empresa_email', form.errors)
    
    def test_empresa_email_is_valid_email(self) -> None:
        """
        Ensure that empresa_email is a valid email.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_email': 'abc123@'})
        self.assertIn('O campo Email da empresa deve conter um email válido.',
            form.errors['empresa_email']
        )
    
    def test_empresa_site_is_required(self) -> None:
        """
        Ensure that empresa_site is required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_site': ''})
        self.assertIn('O campo Site da empresa é obrigatório.', form.errors['empresa_site'])
    
    def test_empresa_site_is_valid_url(self) -> None:
        """
        Ensure that empresa_site is a valid URL.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_site': 'ac123'})
        self.assertIn('O campo Site da empresa deve conter um endereço web válido.',
            form.errors['empresa_site']
        )
    
    def test_empresa_site_accepts_urls_without_protocol(self) -> None:
        """
        Ensure that empresa_site accepts URLs without protocol.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_site': 'foo.com.br'})
        self.assertNotIn('empresa_site', form.errors)
    
    def test_empresa_telefone_celular_is_not_required(self) -> None:
        """
        Ensure that empresa_telefone_celular is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_telefone_celular': ''})
        self.assertNotIn('empresa_telefone_celular', form.errors)
    
    def test_empresa_telefone_celular_is_valid_cellphone(self) -> None:
        """
        Ensure that empresa_telefone_celular is a valid cellphone in the correct format.

        :rtype: None
        """
        expected_error_message = 'O campo Telefone celular da empresa deve conter um número válido. Ex.: (DDD) 99999-9999'

        form = CadastroVagasForm({'empresa_telefone_celular': 't119abc45'})
        self.assertIn(expected_error_message, form.errors['empresa_telefone_celular'])

        form = CadastroVagasForm({'empresa_telefone_celular': '11984510301'})
        self.assertIn(expected_error_message, form.errors['empresa_telefone_celular'])

        form = CadastroVagasForm({'empresa_telefone_celular': '(11) 8451-0301'})
        self.assertIn(expected_error_message, form.errors['empresa_telefone_celular'])

        form = CadastroVagasForm({'empresa_telefone_celular': '(11) 98451-0301'})
        self.assertNotIn('empresa_telefone_celular', form.errors)
    
    def test_empresa_telefone_comercial_is_not_required(self) -> None:
        """
        Ensure that empresa_telefone_comercial is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_telefone_comercial': ''})
        self.assertNotIn('empresa_telefone_comercial', form.errors)
    
    def test_empresa_telefone_comercial_is_valid_landline(self) -> None:
        """
        Ensure that empresa_telefone_comercial is a valid landline in the correct format.

        :rtype: None
        """
        expected_error_message = 'O campo Telefone comercial da empresa deve conter um número válido. Ex.: (DDD) 9999-9999'

        form = CadastroVagasForm({'empresa_telefone_comercial': 't119abc45'})
        self.assertIn(expected_error_message, form.errors['empresa_telefone_comercial'])

        form = CadastroVagasForm({'empresa_telefone_comercial': '1184510301'})
        self.assertIn(expected_error_message, form.errors['empresa_telefone_comercial'])

        form = CadastroVagasForm({'empresa_telefone_comercial': '(11) 8451-0301'})
        self.assertNotIn('empresa_telefone_comercial', form.errors)
    
    def test_cargo_titulo_is_required(self) -> None:
        """
        Ensure that cargo_titulo is required.

        :rtype: None
        """
        form = CadastroVagasForm({'cargo_titulo': ''})
        self.assertIn('O campo Título do cargo é obrigatório.', form.errors['cargo_titulo'])
    
    def test_cargo_descricao_is_not_required(self) -> None:
        """
        Ensure that cargo_descricao is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'cargo_descricao': ''})
        self.assertNotIn('cargo_descricao', form.errors)
    
    def test_site_referencia_is_required(self) -> None:
        """
        Ensure that site_referencia is required.

        :rtype: None
        """
        form = CadastroVagasForm({'site_referencia': ''})
        self.assertIn('O campo Site de referência é obrigatório.', form.errors['site_referencia'])
    
    def test_site_referencia_is_valid_url(self) -> None:
        """
        Ensure that site_referencia is a valid URL.

        :rtype: None
        """
        form = CadastroVagasForm({'site_referencia': 'abc123'})
        self.assertIn('O campo Site de referência deve conter um endereço web válido.',
            form.errors['site_referencia']
        )
    
    def test_site_referencia_accepts_urls_without_protocol(self) -> None:
        """
        Ensure that site_referencia accepts URLs without protocol.

        :rtype: None
        """
        form = CadastroVagasForm({'site_referencia': 'foo.com.br'})
        self.assertNotIn('site_referencia', form.errors)
    
    def test_data_hora_entrevista_is_not_required(self) -> None:
        """
        Ensure that data_hora_entrevista is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'data_hora_entrevista': ''})
        self.assertNotIn('data_hora_entrevista', form.errors)
