import unittest2

def _cria_matriz_do_triangulo(altura):
   dimensoes = range(altura)
   base = range((2 * altura) - 1)
   return [[0 for x in base] for x in dimensoes]

def _le_matriz(matriz, linha, coluna):
    try:
        return matriz[linha][coluna]
    except IndexError:
        return 0

def _povoa_matriz(matriz):
    altura = len(matriz)
    largura = len(matriz[0])
    matriz[0][altura-1] = 1
    for i in range(1, altura):
        for j in range(largura):
            valorAnte = _le_matriz(matriz, i-1, j-1)
            valorProx = _le_matriz(matriz, i-1, j+1)
            matriz[i][j] = valorAnte + valorProx
    return matriz
   
def _formata_matriz_do_triangulo(matriz):
    return str(matriz[0][0])

def triangulo_de_pascal(altura):
    matriz = _cria_matriz_do_triangulo(altura)
    matriz_povoada = _povoa_matriz(matriz)
    return _formata_matriz_do_triangulo(matriz_povoada)

class TrianguloTestCase(unittest2.TestCase):
    def test_altura_1(self):
        self.assertEqual('1', triangulo_de_pascal(1))
        
    def test_altura_2(self):
        self.assertEqual(' 1\n1 1', triangulo_de_pascal(2))

if __name__ == '__main__':
    unittest2.main(verbosity=2)
