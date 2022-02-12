from django.test import TestCase
from vagas.models import Vaga

class VagaModelTest(TestCase):
    """Tests for model Vaga."""

    def setUp(self) -> None:
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
            data_hora_entrevista='20/01/2022 15:30',
        )
        return super().setUp()

    def test_create_vaga(self) -> None:
        """
        Test creation of model Vaga.

        :return: None
        """
        self.assertIsNotNone(self.vaga.id)
        self.assertEqual('Minha empresa', self.vaga.empresa_nome)
        self.assertEqual('Meu endereço', self.vaga.empresa_endereco)
        self.assertEqual('meuemail@email.com', self.vaga.empresa_email)
        self.assertEqual('https://meusite.com.br', self.vaga.empresa_site)
        self.assertEqual('(11) 98765-3201', self.vaga.empresa_telefone_celular)
        self.assertEqual('(11) 8765-3201', self.vaga.empresa_telefone_comercial)
        self.assertEqual('Título do cargo', self.vaga.cargo_titulo)
        self.assertEqual('Descrição do cargo', self.vaga.cargo_descricao)
        self.assertEqual('https://sitereferencia.com.br', self.vaga.site_referencia)
        self.assertEqual('20/01/2022 15:30', self.vaga.data_hora_entrevista)
    
    def test_str_representation(self) -> None:
        """
        Test __str__ method on model Vaga.

        :return: None
        """
        self.assertEqual(self.vaga.empresa_nome, str(self.vaga))
    
    def test_get_absolute_url(self) -> None:
        """
        Test get_absolute_url method on model Vaga

        :return: None
        """
        self.assertEqual(f'/oportunidades/{str(self.vaga.id)}', self.vaga.get_absolute_url())
    
    def test_empresa_telefone_celular_is_stored_with_digits_only(self) -> None:
        """
        Ensure that field empresa_telefone_celular is stored with digits only.

        :return: None
        """
        vaga = Vaga.objects.get(pk=self.vaga.id)
        self.assertRegexpMatches(vaga.empresa_telefone_celular, '^\d{11}$')
    
    def test_empresa_telefone_comercial_is_stored_with_digits_only(self) -> None:
        """
        Ensure that field empresa_telefone_comercial is store with digits only.

        :return: None
        """
        vaga = Vaga.objects.get(pk=self.vaga.id)
        self.assertRegexpMatches(vaga.empresa_telefone_comercial, '^\d{10}$')