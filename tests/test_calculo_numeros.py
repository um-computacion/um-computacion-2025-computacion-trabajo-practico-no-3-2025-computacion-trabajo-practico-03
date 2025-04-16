import unittest
from unittest.mock import patch

# Agregamos los tests para el ingreso de texto no numericos 
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

 
    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo_entero(self, patch_input):
        """Prueba el caso de ingreso de un número entero negativo"""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch('builtins.input', return_value='-0.5')
    def test_ingreso_negativo_decimal(self, patch_input):
        """Prueba el caso de ingreso de un número decimal negativo"""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch('builtins.input', return_value='-0.0')
    def test_ingreso_negativo_cero(self, patch_input):
        """Prueba el caso de ingreso de cero negativo"""
        numero = ingrese_numero()
        self.assertEqual(numero, 0)
        
    @patch('builtins.input', return_value='  -42  ')
    def test_ingreso_negativo_con_espacios(self, patch_input):
        """Prueba el caso de ingreso de número negativo con espacios"""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()


    @patch('builtins.input', return_value='ABC')
    def test_ingreso_texto_no_numerico(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='ABC')
    def test_ingreso_texto_simple(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='12AB')
    def test_ingreso_mixto_numero_texto(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='')
    def test_ingreso_vacio(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value=' ')
    def test_ingreso_espacio_blanco(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='@#!')
    def test_ingreso_caracteres_especiales(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()


if __name__ == '__main__':
    unittest.main()

