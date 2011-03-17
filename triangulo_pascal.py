import unittest2 as unittest

def problema_para_resolver(parametro):
    return 1 == parametro

class TestSequenceFunctions(unittest.TestCase):
    def test_simples(self):
        self.assertEqual(True, problema_para_resolver(1))

if __name__ == '__main__':
    unittest.main(verbosity=2)
