from django.test import TestCase
from django.utils import timezone
from vagas.models import Vaga

class VagaModelTest(TestCase):
    """Tests for model Vaga."""

    def setUp(self) -> None:
        self.now = timezone.now()
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
            data_hora_entrevista=timezone.now(),
        )
    
    def test_str_representation(self) -> None:
        """
        Test __str__ method on model Vaga.

        :rtype: None
        """
        self.assertEqual(self.vaga.empresa_nome, str(self.vaga))
    
    def test_get_absolute_url(self) -> None:
        """
        Test get_absolute_url method on model Vaga

        :rtype: None
        """
        self.assertEqual(f'/oportunidades/{str(self.vaga.pk)}', self.vaga.get_absolute_url())
    
    def test_empresa_telefone_celular_is_stored_with_digits_only(self) -> None:
        """
        Ensure that field empresa_telefone_celular is stored with digits only.

        :rtype: None
        """
        vaga = Vaga.objects.get(pk=self.vaga.pk)
        self.assertRegexpMatches(vaga.empresa_telefone_celular, '^\d{11}$')
    
    def test_empresa_telefone_comercial_is_stored_with_digits_only(self) -> None:
        """
        Ensure that field empresa_telefone_comercial is stored with digits only.

        :rtype: None
        """
        vaga = Vaga.objects.get(pk=self.vaga.pk)
        self.assertRegexpMatches(vaga.empresa_telefone_comercial, '^\d{10}$')
    
    def test_has_auto_filled_data_hora_cadastro_field(self) -> None:
        """
        Ensure model has datetime field data_hora_cadastro which is automatically filled upon creation.

        :rtype: None
        """
        vaga = Vaga.objects.get(pk=self.vaga.pk)
        self.assertGreaterEqual(vaga.data_hora_cadastro, self.now)