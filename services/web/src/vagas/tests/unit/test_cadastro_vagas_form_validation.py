from django.test import SimpleTestCase
from django.utils import timezone
import datetime as dt
from vagas.forms import CadastroVagasForm
from vagas.models import Vaga

class CadastroVagasFormValidationTest(SimpleTestCase):
    """Ensure CadastroVagasForm performs the necessary validation."""
    
    def test_empresa_nome_is_required(self) -> None:
        """
        Ensure that empresa_nome is required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_nome': ''})
        self.assertIn('O campo Nome da empresa é obrigatório.', form.errors['empresa_nome'])
    
    def test_empresa_nome_cannot_exceed_maximum_length(self) -> None:
        """
        Ensure that empresa_nome cannot exceed its maximum length.

        :rtype: None
        """
        empresa_nome1 = 'X' * 101
        form1 = CadastroVagasForm({'empresa_nome': empresa_nome1})
        self.assertIn('O campo Nome da empresa pode conter no máximo 100 caracteres.',
            form1.errors['empresa_nome'])
        
        empresa_nome2 = 'X' * 100
        form2 = CadastroVagasForm({'empresa_nome': empresa_nome2})
        self.assertNotIn('empresa_nome', form2.errors)
    
    def test_empresa_endereco_is_not_required(self) -> None:
        """
        Ensure that empresa_endereco is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_endereco': ''})
        self.assertNotIn('empresa_endereco', form.errors)
    
    def test_empresa_endereco_cannot_exceed_maximum_length(self) -> None:
        """
        Ensure that empresa_endereco cannot exceed its maximum length.

        :rtype: None
        """
        empresa_endereco1 = 'X' * 201
        form1 = CadastroVagasForm({'empresa_endereco': empresa_endereco1})
        self.assertIn('O campo Endereço da empresa pode conter no máximo 200 caracteres.',
            form1.errors['empresa_endereco'])
        
        empresa_endereco2 = 'X' * 200
        form2 = CadastroVagasForm({'empresa_endereco': empresa_endereco2})
        self.assertNotIn('empresa_endereco', form2.errors)
    
    def test_empresa_email_is_not_required(self) -> None:
        """
        Ensure that empresa_email is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_email': ''})
        self.assertNotIn('empresa_email', form.errors)
    
    def test_empresa_email_must_be_valid_email(self) -> None:
        """
        Ensure that empresa_email must be a valid email.

        :rtype: None
        """
        form1 = CadastroVagasForm({'empresa_email': 'abc123@'})
        self.assertIn('O campo Email da empresa deve conter um email válido.',
            form1.errors['empresa_email']
        )

        form2 = CadastroVagasForm({'empresa_email': 'foo@email.com'})
        self.assertNotIn('empresa_email', form2.errors)
    
    def test_empresa_site_is_required(self) -> None:
        """
        Ensure that empresa_site is required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_site': ''})
        self.assertIn('O campo Site da empresa é obrigatório.', form.errors['empresa_site'])
    
    def test_empresa_site_must_be_valid_url(self) -> None:
        """
        Ensure that empresa_site must be a valid URL.

        :rtype: None
        """
        form1 = CadastroVagasForm({'empresa_site': 'ac123'})
        self.assertIn('O campo Site da empresa deve conter um endereço web válido.',
            form1.errors['empresa_site']
        )

        form2 = CadastroVagasForm({'empresa_site': 'https://foo.com'})
        self.assertNotIn('empresa_site', form2.errors)
    
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
    
    def test_empresa_telefone_celular_must_be_valid_cellphone(self) -> None:
        """
        Ensure that empresa_telefone_celular must be a valid cellphone in the correct format.

        :rtype: None
        """
        expected_error_message = 'O campo Telefone celular da empresa deve conter um número válido. Ex.: (DDD) 99999-9999'

        form1 = CadastroVagasForm({'empresa_telefone_celular': 't119abc45'})
        self.assertIn(expected_error_message, form1.errors['empresa_telefone_celular'])

        form2 = CadastroVagasForm({'empresa_telefone_celular': '11984510301'})
        self.assertIn(expected_error_message, form2.errors['empresa_telefone_celular'])

        form3 = CadastroVagasForm({'empresa_telefone_celular': '(11) 8451-0301'})
        self.assertIn(expected_error_message, form3.errors['empresa_telefone_celular'])

        form4 = CadastroVagasForm({'empresa_telefone_celular': '(11) 98451-0301'})
        self.assertNotIn('empresa_telefone_celular', form4.errors)
    
    def test_empresa_telefone_comercial_is_not_required(self) -> None:
        """
        Ensure that empresa_telefone_comercial is not required.

        :rtype: None
        """
        form = CadastroVagasForm({'empresa_telefone_comercial': ''})
        self.assertNotIn('empresa_telefone_comercial', form.errors)
    
    def test_empresa_telefone_comercial_must_be_valid_landline(self) -> None:
        """
        Ensure that empresa_telefone_comercial must be a valid landline in the correct format.

        :rtype: None
        """
        expected_error_message = 'O campo Telefone comercial da empresa deve conter um número válido. Ex.: (DDD) 9999-9999'

        form1 = CadastroVagasForm({'empresa_telefone_comercial': 't119abc45'})
        self.assertIn(expected_error_message, form1.errors['empresa_telefone_comercial'])

        form2 = CadastroVagasForm({'empresa_telefone_comercial': '1184510301'})
        self.assertIn(expected_error_message, form2.errors['empresa_telefone_comercial'])

        form3 = CadastroVagasForm({'empresa_telefone_comercial': '(11) 8451-0301'})
        self.assertNotIn('empresa_telefone_comercial', form3.errors)
    
    def test_cargo_titulo_is_required(self) -> None:
        """
        Ensure that cargo_titulo is required.

        :rtype: None
        """
        form = CadastroVagasForm({'cargo_titulo': ''})
        self.assertIn('O campo Título do cargo é obrigatório.', form.errors['cargo_titulo'])
    
    def test_cargo_titulo_cannot_exceed_maximum_length(self) -> None:
        """
        Ensure that cargo_titulo cannot exceed its maximum length.

        :rtype: None
        """
        cargo_titulo1 = 'X' * 51
        form1 = CadastroVagasForm({'cargo_titulo': cargo_titulo1})
        self.assertIn('O campo Título do cargo pode conter no máximo 50 caracteres.',
            form1.errors['cargo_titulo'])
        
        cargo_titulo2 = 'X' * 50
        form2 = CadastroVagasForm({'cargo_titulo': cargo_titulo2})
        self.assertNotIn('cargo_titulo', form2.errors)
    
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
    
    def test_site_referencia_must_be_valid_url(self) -> None:
        """
        Ensure that site_referencia must be a valid URL.

        :rtype: None
        """
        form1 = CadastroVagasForm({'site_referencia': 'abc123'})
        self.assertIn('O campo Site de referência deve conter um endereço web válido.',
            form1.errors['site_referencia']
        )

        form2 = CadastroVagasForm({'site_referencia': 'http://foo.com'})
        self.assertNotIn('site_referencia', form2.errors)
    
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
    
    def test_data_hora_entrevista_must_be_valid_datetime(self) -> None:
        """
        Ensure that data_hora_entrevista must be a valid datetime in the correct format.

        :rtype: None
        """
        expected_error_message = 'O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos'

        form1 = CadastroVagasForm({'data_hora_entrevista': 'abc123'})
        self.assertIn(expected_error_message, form1.errors['data_hora_entrevista'])

        form2 = CadastroVagasForm({'data_hora_entrevista': '32/02/2022 15:11'})
        self.assertIn(expected_error_message, form2.errors['data_hora_entrevista'])

        form3 = CadastroVagasForm({'data_hora_entrevista': '2022/10/02 09:06'})
        self.assertIn(expected_error_message, form3.errors['data_hora_entrevista'])

        form4 = CadastroVagasForm({'data_hora_entrevista': '14/05/22 06:01'})
        self.assertIn(expected_error_message, form4.errors['data_hora_entrevista'])

        form5 = CadastroVagasForm({'data_hora_entrevista': timezone.localtime().strftime('%d/%m/%Y %H:%M')})
        self.assertNotIn('data_hora_entrevista', form5.errors)

        form6 = CadastroVagasForm({'data_hora_entrevista': timezone.localtime()})
        self.assertNotIn('data_hora_entrevista', form6.errors)
    
    def test_situacao_is_required(self) -> None:
        """
        Ensure that situacao is required.

        :rtype: None
        """
        form = CadastroVagasForm({'situacao': ''})
        self.assertIn('O campo Situação é obrigatório.', form.errors['situacao'])
    
    def test_situacao_cannot_contain_invalid_value(self) -> None:
        """
        Ensure that situacao cannot contain an invalid value

        :rtype: None
        """
        form = CadastroVagasForm({'situacao': 'foo'})
        self.assertIn('O campo Situação contém um valor inválido.', form.errors['situacao'])
    
    def test_data_hora_entrevista_must_be_blank_if_situacao_is_applied(self) -> None:
        """
        Ensure that data_hora_entrevista must be blank if situacao has a value of Vaga.Status.APPLIED.

        :rtype: None
        """
        form = CadastroVagasForm({
            'situacao': Vaga.Status.APPLIED,
            'data_hora_entrevista': timezone.localtime(),
        })
        self.assertIn("O campo Data e horário da entrevista deve estar vazio caso a situação do cadastro seja 'Candidatado'.",
            form.errors['data_hora_entrevista']
        )
    
    def test_data_hora_entrevista_cannot_be_blank_if_situacao_is_interview_scheduled(self) -> None:
        """
        Ensure that data_hora_entrevista cannot be blank if situacao has a value of Vaga.Status.INTERVIEW_SCHEDULED.

        :rtype: None
        """
        form = CadastroVagasForm({
            'situacao': Vaga.Status.INTERVIEW_SCHEDULED,
            'data_hora_entrevista': '',
        })
        self.assertIn("O campo Data e o horário da entrevista deve ser preenchido caso a situação do cadastro seja 'Entrevista agendada'.",
            form.errors['data_hora_entrevista']
        )
    
    def test_data_hora_entrevista_must_be_equal_to_or_later_than_current_datetime_if_situacao_is_interview_scheduled(self) -> None:
        """
        Ensure that data_hora_entrevista must be equal to or later than current datetime if situacao has a value of Vaga.Status.INTERVIEW_SCHEDULED.

        :rtype: None
        """
        before = timezone.localtime() - dt.timedelta(minutes=3)
        form = CadastroVagasForm({
            'situacao': Vaga.Status.INTERVIEW_SCHEDULED,
            'data_hora_entrevista': before,
        })
        self.assertIn('O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.',
            form.errors['data_hora_entrevista']
        )

        form = CadastroVagasForm({
            'situacao': Vaga.Status.INTERVIEW_SCHEDULED,
            'data_hora_entrevista': timezone.localtime(),
        })
        self.assertNotIn('data_hora_entrevista', form.errors)

        after = timezone.localtime() + dt.timedelta(minutes=3)
        form = CadastroVagasForm({
            'situacao': Vaga.Status.INTERVIEW_SCHEDULED,
            'data_hora_entrevista': after,
        })
        self.assertNotIn('data_hora_entrevista', form.errors)