import unittest
from src.calculo_numeros import ingrese_numero
from src.exceptions import NumeroDebeSerPositivo

from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='-100')
    def test_numero_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='abc')
    def test_input_invalido(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

