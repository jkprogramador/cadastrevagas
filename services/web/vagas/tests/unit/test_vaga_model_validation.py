from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime as dt
from vagas.models import Vaga

class VagaModelValidationTest(TestCase):
    """Ensure that model Vaga performs the necessary validation."""

    def setUp(self) -> None:
        self.all_fields = {
            'empresa_nome',
            'empresa_endereco',
            'empresa_email',
            'empresa_site',
            'empresa_telefone_celular',
            'empresa_telefone_comercial',
            'cargo_titulo',
            'cargo_descricao',
            'site_referencia',
            'data_hora_entrevista'
        }

    def test_empresa_nome_cannot_be_blank(self) -> None:
        """
        Ensure that empresa_nome cannot be blank.

        :rtype: None
        """
        vaga = Vaga(empresa_nome='')
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'empresa_nome'})
        
        self.assertIn('O campo Nome da empresa é obrigatório.',
            ctx.exception.message_dict['empresa_nome'])
    
    def test_empresa_nome_cannot_exceed_max_length(self) -> None:
        """
        Ensure that empresa_nome cannot exceed its maximum length.

        :rtype: None
        """
        empresa_nome = 'X' * 101
        vaga = Vaga(empresa_nome=empresa_nome)
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'empresa_nome'})
        
        self.assertIn('O campo Nome da empresa pode conter no máximo 100 caracteres.',
            ctx.exception.message_dict['empresa_nome'])
    
    def test_empresa_endereco_can_be_blank(self) -> None:
        """
        Ensure that empresa_endereco can be blank.

        :rtype: None
        """
        vaga = Vaga(empresa_endereco='')
        vaga.clean_fields(exclude=self.all_fields - {'empresa_endereco'})
        self.assertEqual('', vaga.empresa_endereco)
    
    def test_empresa_endereco_cannot_exceed_max_length(self) -> None:
        """
        Ensure that empresa_endereco cannot exceed its maximum length.

        :rtype: None
        """
        empresa_endereco = 'X' * 201
        vaga = Vaga(empresa_endereco=empresa_endereco)
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'empresa_endereco'})
        
        self.assertIn('O campo Endereço da empresa pode conter no máximo 200 caracteres.',
            ctx.exception.message_dict['empresa_endereco'])
    
    def test_empresa_email_can_be_blank(self) -> None:
        """
        Ensure that empresa_email can be blank.

        :rtype: None
        """
        vaga = Vaga(empresa_email='')
        vaga.clean_fields(exclude=self.all_fields - {'empresa_email'})
        self.assertEqual('', vaga.empresa_email)
    
    def test_empresa_email_must_be_valid_email(self) -> None:
        """
        Ensure that empresa_email must be a valid email.

        :rtype: None
        """
        vaga = Vaga(empresa_email='email@')
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'empresa_email'})
        
        self.assertIn('O campo Email da empresa deve conter um email válido.',
            ctx.exception.message_dict['empresa_email'])
    
    def test_empresa_site_cannot_be_blank(self) -> None:
        """
        Ensure that empresa_site cannot be blank.

        :rtype: None
        """
        vaga = Vaga(empresa_site='')
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'empresa_site'})
        
        self.assertIn('O campo Site da empresa é obrigatório.',
            ctx.exception.message_dict['empresa_site'])
    
    def test_empresa_site_must_be_valid_url(self) -> None:
        """
        Ensure that empresa_site must be a valid URL.

        :rtype: None
        """
        vaga = Vaga(empresa_site='foo.')
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'empresa_site'})
        
        self.assertIn('O campo Site da empresa deve conter um endereço web válido.',
            ctx.exception.message_dict['empresa_site'])
    
    def test_empresa_site_must_be_url_with_protocol(self) -> None:
        """
        Ensure that empresa_site must be a URL with protocol.

        :rtype: None
        """
        vaga = Vaga(empresa_site='www.foo.com.br')
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'empresa_site'})
        
        self.assertIn('O campo Site da empresa deve conter um endereço web válido.',
            ctx.exception.message_dict['empresa_site'])
    
    def test_empresa_telefone_celular_can_be_blank(self) -> None:
        """
        Ensure that empresa_telefone_celular can be blank.

        :rtype: None
        """
        vaga = Vaga(empresa_telefone_celular='')
        vaga.clean_fields(exclude=self.all_fields - {'empresa_telefone_celular'})
        self.assertEqual('', vaga.empresa_telefone_celular)
    
    def test_empresa_telefone_celular_must_be_valid_cellphone(self) -> None:
        """
        Ensure that empresa_telefone_celular must be a valid cellphone.

        :rtype: None
        """
        expected_error_message = 'O campo Telefone celular da empresa deve conter um número válido. Ex.: (DDD) 99999-9999'

        vaga1 = Vaga(empresa_telefone_celular='ab5kT48')
        
        with self.assertRaises(ValidationError) as ctx1:
            vaga1.clean_fields(exclude=self.all_fields - {'empresa_telefone_celular'})
        
        self.assertIn(expected_error_message, ctx1.exception.message_dict['empresa_telefone_celular'])
        
        vaga2 = Vaga(empresa_telefone_celular='11948520325')
        
        with self.assertRaises(ValidationError) as ctx2:
            vaga2.clean_fields(exclude=self.all_fields - {'empresa_telefone_celular'})
        
        self.assertIn(expected_error_message, ctx2.exception.message_dict['empresa_telefone_celular'])

        expected_phone = '(11) 94852-0325'
        vaga3 = Vaga(empresa_telefone_celular=expected_phone)
        vaga3.clean_fields(exclude=self.all_fields - {'empresa_telefone_celular'})
        self.assertEqual(expected_phone, vaga3.empresa_telefone_celular)
    
    def test_empresa_telefone_comercial_can_be_blank(self) -> None:
        """
        Ensure that empresa_telefone_comercial can be blank.

        :rtype: None
        """
        vaga = Vaga(empresa_telefone_comercial='')
        vaga.clean_fields(exclude=self.all_fields - {'empresa_telefone_comercial'})
        self.assertEqual('', vaga.empresa_telefone_comercial)

    def test_empresa_telefone_comercial_must_be_valid_landline(self) -> None:
        """
        Ensure that empresa_telefone_comercial must be a valid landline.

        :rtype: None
        """
        expected_error_message = 'O campo Telefone comercial da empresa deve conter um número válido. Ex.: (DDD) 9999-9999'

        vaga1 = Vaga(empresa_telefone_comercial='ab5kT48')
        
        with self.assertRaises(ValidationError) as ctx1:
            vaga1.clean_fields(exclude=self.all_fields - {'empresa_telefone_comercial'})
        
        self.assertIn(expected_error_message, ctx1.exception.message_dict['empresa_telefone_comercial'])
        
        vaga2 = Vaga(empresa_telefone_comercial='1148520325')
        
        with self.assertRaises(ValidationError) as ctx2:
            vaga2.clean_fields(exclude=self.all_fields - {'empresa_telefone_comercial'})
        
        self.assertIn(expected_error_message, ctx2.exception.message_dict['empresa_telefone_comercial'])

        expected_phone = '(11) 4852-0325'
        vaga3 = Vaga(empresa_telefone_comercial=expected_phone)
        vaga3.clean_fields(exclude=self.all_fields - {'empresa_telefone_comercial'})
        self.assertEqual(expected_phone, vaga3.empresa_telefone_comercial)
    
    def test_cargo_titulo_cannot_be_blank(self) -> None:
        """
        Ensure that cargo_titulo cannot be blank.

        :rtype: None
        """
        vaga = Vaga(cargo_titulo='')
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'cargo_titulo'})
        
        self.assertIn('O campo Título do cargo é obrigatório.', ctx.exception.message_dict['cargo_titulo'])
    
    def test_cargo_titulo_cannot_exceed_maximum_length(self) -> None:
        """
        Ensure that cargo_titulo cannot exceed its maximum length.

        :rtype: None
        """
        cargo_titulo = 'X' * 51
        vaga = Vaga(cargo_titulo=cargo_titulo)
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'cargo_titulo'})
        
        self.assertIn('O campo Título do cargo pode conter no máximo 50 caracteres.',
            ctx.exception.message_dict['cargo_titulo'])
    
    def test_cargo_descricao_can_be_blank(self) -> None:
        """
        Ensure that cargo_descricao can be blank.

        :rtype: None
        """
        vaga = Vaga(cargo_descricao='')
        vaga.clean_fields(exclude=self.all_fields - {'cargo_descricao'})
        self.assertEqual('', vaga.cargo_descricao)
    
    def test_site_referencia_cannot_be_blank(self) -> None:
        """
        Ensure that site_referencia cannot be blank.

        :rtype: None
        """
        vaga = Vaga(site_referencia='')
        with self.assertRaises(ValidationError) as ctx:
            vaga.clean_fields(exclude=self.all_fields - {'site_referencia'})
        
        self.assertIn('O campo Site de referência é obrigatório.',
            ctx.exception.message_dict['site_referencia'])
    
    def test_site_referencia_must_be_valid_url(self) -> None:
        """
        Ensure that site_referencia must be a valid URL.

        :rtype: None
        """
        vaga1 = Vaga(site_referencia='foo.')
        with self.assertRaises(ValidationError) as ctx:
            vaga1.clean_fields(exclude=self.all_fields - {'site_referencia'})
        
        self.assertIn('O campo Site de referência deve conter um endereço web válido.',
            ctx.exception.message_dict['site_referencia'])
        
        expected_site_referencia = 'http://foo.com'
        vaga2 = Vaga(site_referencia=expected_site_referencia)
        vaga2.clean_fields(exclude=self.all_fields - {'site_referencia'})
        self.assertEqual(expected_site_referencia, vaga2.site_referencia)
    
    def test_data_hora_entrevista_can_be_blank(self) -> None:
        """
        Ensure that data_hora_entrevista can be blank.

        :rtype: None
        """
        vaga = Vaga(data_hora_entrevista='')
        vaga.clean_fields(exclude=self.all_fields - {'data_hora_entrevista'})
        self.assertEqual('', vaga.data_hora_entrevista)
    
    def test_data_hora_entrevista_must_be_valid_datetime(self) -> None:
        """
        Ensure that data_hora_entrevista must be a valid datetime.

        :rtype: None
        """
        vaga1 = Vaga(data_hora_entrevista='2022-02-32 09:04')
        with self.assertRaises(ValidationError) as ctx1:
            vaga1.clean_fields(exclude=self.all_fields - {'data_hora_entrevista'})
        
        self.assertIn('O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos',
            ctx1.exception.message_dict['data_hora_entrevista'])
        
        a_datetime = timezone.now()
        vaga2 = Vaga(data_hora_entrevista=a_datetime)
        vaga2.clean_fields(exclude=self.all_fields - {'data_hora_entrevista'})
        self.assertEqual(a_datetime, vaga2.data_hora_entrevista)

    def test_blank_data_hora_entrevista_must_be_equal_to_or_later_than_current_datetime(self) -> None:
        """
        Ensure that a blank data_hora_entrevista must be greater than or equal to current datetime.

        :rtype: None
        """
        prior_to_now1 = timezone.localtime() - dt.timedelta(minutes=5)
        vaga1 = Vaga(data_hora_entrevista=prior_to_now1)
        with self.assertRaises(ValidationError) as ctx1:
            vaga1.full_clean(exclude=self.all_fields - {'data_hora_entrevista'})
        
        self.assertIn('O campo Data e horário da entrevista não pode ser anterior à data e ao horário atuais.',
            ctx1.exception.message_dict['data_hora_entrevista'])
    
    def test_existing_data_hora_entrevista_can_be_any_datetime(self) -> None:
        """
        Ensure that an existing data_hora_entrevista can be any datetime.

        :rtype: None
        """
        vaga = Vaga.objects.create(
            empresa_nome='Minha empresa',
            empresa_site='https://meusite.com.br',
            cargo_titulo='Título do cargo',
            site_referencia='https://sitereferencia.com.br',
            data_hora_entrevista=timezone.localtime(),
        )
        before_current_datetime = timezone.localtime() - dt.timedelta(minutes=5)
        with self.assertRaises(ValidationError) as ctx_1:
            vaga.empresa_nome = ''
            vaga.data_hora_entrevista = before_current_datetime
            vaga.full_clean()
        
        self.assertNotIn('data_hora_entrevista', ctx_1.exception.message_dict)