import unittest
from src.calculo_numeros import Ingrese_Numero
from src.exceptions import NumeroDebeSerPositivo
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = Ingrese_Numero()
        self.assertEqual(numero, 100)

    #@patch('builtins.input', return_value='-100')
    #def test_ingreso_negativo(self, patch_input):
       # with self.assertRaises(NumeroDebeSerPositivo):
            #Ingrese_Numero()

   # @patch('builtins.input', return_value='AAA')
    #def test_ingreso_letras(self, patch_input):
        #with self.assertRaises(ValueError):
            #Ingrese_Numero()

if __name__ == '__main__':
    unittest.main()
