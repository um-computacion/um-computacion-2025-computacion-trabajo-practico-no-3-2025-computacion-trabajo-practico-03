import unittest
from unittest.mock import patch

from src.exceptions import ingrese_numero

class TestCalculoNumeros(unittest.TestCase):
    
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

if __name__ == '__main__':
    unittest.main()