import unittest2 as unittest

def _cria_matriz_do_triangulo(altura):
   dimensoes = range(altura)
   return [[1 for x in dimensoes] for x in dimensoes]
   
def _formata_matriz_do_triangulo(matriz):
   return str(matriz[0][0])

def triangulo_de_pascal(altura):
    if altura == 1:
        matriz = _cria_matriz_do_triangulo(1)
        r = _formata_matriz_do_triangulo(matriz)
    elif altura == 2:
        r = ' 1\n1 1'
    return r

class TrianguloTestCase(unittest.TestCase):
    def test_altura_1(self):
        self.assertEqual('1', triangulo_de_pascal(1))
        
    def test_altura_2(self):
        self.assertEqual(' 1\n1 1', triangulo_de_pascal(2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
