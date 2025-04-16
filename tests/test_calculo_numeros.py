import unittest
from unittest.mock import patch

# Estos imports fallarán inicialmente porque estamos siguiendo TDD
# y aún no hemos creado los archivos de implementación
from src.exceptions import NumeroDebeSerPositivo
from src.calculo_numeros import ingrese_numero

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        """Prueba el caso de ingreso de un número positivo válido"""
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        """Prueba el caso de ingreso de un número negativo"""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        """Prueba el caso de ingreso de texto no numérico"""
        with self.assertRaises(ValueError):
            ingrese_numero()
    
    @patch('builtins.input', return_value='0')
    def test_ingreso_cero(self, patch_input):
        """Prueba el caso de ingreso del número cero (límite)"""
        numero = ingrese_numero()
        self.assertEqual(numero, 0)
        
    @patch('builtins.input', return_value='   50   ')
    def test_ingreso_con_espacios(self, patch_input):
        """Prueba el caso con espacios en blanco"""
        numero = ingrese_numero()
        self.assertEqual(numero, 50)

if __name__ == '__main__':
    unittest.main()

