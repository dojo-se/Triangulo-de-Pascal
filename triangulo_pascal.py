import unittest2 as unittest

def triangulo_de_pascal(parametro):
    return '1'

class TrianguloTestCase(unittest.TestCase):
    def test_altura_1(self):
        self.assertEqual('1', triangulo_de_pascal(1))

if __name__ == '__main__':
    unittest.main(verbosity=2)
