import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    # Issue 1: Tests para números válidos (con 100, 50, 20 y 10)
    @patch(  # Este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_100(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch(  # Este patch controla lo que hace el input
        'builtins.input',
        return_value='50'
    )
    def test_ingreso_50(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 50)

    @patch(  # Este patch controla lo que hace el input
        'builtins.input',
        return_value='20'
    )
    def test_ingreso_20(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 20)

    @patch(  # Este patch controla lo que hace el input
        'builtins.input',
        return_value='10'
    )
    def test_ingreso_10(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 10)


    
    # Issue 2: Agregar tests para ingreso de números negativos
    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo_100(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-50')
    def test_ingreso_negativo_50(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-20')
    def test_ingreso_negativo_20(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch( 'builtins.input', return_value='-10')
    def test_ingreso_negativo_10(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    # Issue 3: Tests para texto no numérico
    @patch('builtins.input',return_value='AAA')
    def test_ingreso_texto(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input',return_value='abc')
    def test_ingreso_abc(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input',return_value='!@#')
    def test_ingreso_caracteres_especiales(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='-10')
    def test_ingreso_negativo_10(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    

if __name__ == '__main__':
    unittest.main()

