import unittest
from src.calculo_numeros import ingrese_numero
from src.exceptions import NumeroDebeSerPositivo

from unittest.mock import patch

class TestNumeroValido(unittest.TestCase):
    
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    
    @patch('builtins.input', return_value='25')
    def test_ingreso_feliz_25(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 25)
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='-100'
    )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo) as contexto:
            ingrese_numero()
        self.assertEqual(str(contexto.exception), 'El número debe ser positivo')
    
    @patch(  # Este patch controla lo que hace el input
        'builtins.input',
        return_value='AAA'  # Simula que el usuario ingresa 'AAA'
    )
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

  
    @patch(  # Este patch controla lo que hace el input
        'builtins.input',
        return_value='123abc'  # Simula que el usuario ingresa '123abc'
    )
    def test_ingreso_numero_con_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch(  # Este patch controla lo que hace el input
        'builtins.input',
        return_value='!@#'  # Simula que el usuario ingresa caracteres especiales
    )
    def test_ingreso_caracteres_especiales(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()
