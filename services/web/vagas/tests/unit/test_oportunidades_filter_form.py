from django.test import SimpleTestCase
from django.forms import ChoiceField
from vagas.forms import OportunidadesFilterForm

class OportunidadesFilterFormTest(SimpleTestCase):
    """Test to ensure that the form for filtering job opportunities has the required fields."""

    def setUp(self) -> None:
        self.form = OportunidadesFilterForm()
    
    def test_has_choice_field_situacao(self) -> None:
        """
        Ensure form has choice field for selecting the status of a job opportunity.

        :rtype: None
        """
        situacao = self.form.fields['situacao']
        self.assertIsInstance(situacao, ChoiceField)
        self.assertIn(('W', 'Aguardando retorno',), situacao.choices)
        self.assertIn(('S', 'Entrevista agendada',), situacao.choices)
        self.assertIn(('R', 'Rejeitado',), situacao.choices)
        self.assertIn((None, 'Todas',), situacao.choices)
        self.assertEqual((None, 'Todas',), situacao.initial)