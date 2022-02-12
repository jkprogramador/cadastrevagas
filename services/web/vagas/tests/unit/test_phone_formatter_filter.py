import unittest
from vagas.templatetags.vagas_template_extras import phone_formatter

class PhoneFormatterFilterTest(unittest.TestCase):
    """Tests for phone formatter filter."""
    
    def test_phone_formatter_returns_correct_cellphone_format(self) -> None:
        """
        Ensure that phone formatter filter returns correct format for a cellphone.

        :return: None
        """
        cellphone = '11987653201'
        formatted_cellphone = phone_formatter(cellphone)
        self.assertEqual('(11) 98765-3201', formatted_cellphone)
    
    def test_phone_formatter_returns_correct_landline_format(self) -> None:
        """
        Ensure that phone formatter filter returns correct format for a landline.

        :return: None
        """
        landline = '1187653201'
        formatted_landline = phone_formatter(landline)
        self.assertEqual('(11) 8765-3201', formatted_landline)