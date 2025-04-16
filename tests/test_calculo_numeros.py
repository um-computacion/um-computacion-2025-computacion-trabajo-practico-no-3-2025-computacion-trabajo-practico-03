import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    
    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        from src.exceptions import ingrese_numero, NumeroDebeSerPositivo
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()