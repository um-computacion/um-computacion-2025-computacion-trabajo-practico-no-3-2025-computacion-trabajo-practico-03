import unittest
from unittest.mock import patch
from src.exceptions import NumeroDebeSerPositivo
from src.calculo_numeros import ingrese_numero

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()