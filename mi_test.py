import unittest

from prueba import Prueba


class MiTest(unittest.TestCase):

    def test_hola_mundo(self):
        prueba = Prueba()
        self.assertEqual(prueba.saludo(), 'Hola Mundo')


if __name__ == '__main__':
    unittest.main()
