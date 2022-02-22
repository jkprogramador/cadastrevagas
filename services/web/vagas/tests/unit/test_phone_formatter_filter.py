import unittest
from vagas.templatetags.vagas_template_extras import phone_formatter

class PhoneFormatterFilterTest(unittest.TestCase):
    """Tests for phone formatter filter."""
    
    def test_phone_formatter_returns_correct_cellphone_format(self) -> None:
        """
        Ensure that phone formatter filter returns correct format for a cellphone.

        :rtype: None
        """
        expected = '(11) 98765-3201'
        actual = phone_formatter('11987653201')
        self.assertEqual(expected, actual)
    
    def test_phone_formatter_returns_correct_landline_format(self) -> None:
        """
        Ensure that phone formatter filter returns correct format for a landline.

        :rtype: None
        """
        expected = '(11) 8765-3201'
        actual = phone_formatter('1187653201')
        self.assertEqual(expected, actual)