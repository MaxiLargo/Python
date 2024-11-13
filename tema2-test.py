import unittest
from queue import Queue as Cola

from Template_t2 import gestion_ventas, cantidad_digitos_impares, reordenar_cola_primero_numerosas, matriz_cuasi_decreciente

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
    
Para ejecutar coverage, ejecutar:
		coverage run --branch --include=ejercicios.py -m unittest test_suite.py

Importante: el nombre de cada caso de test debe comenzar con 'test' para que unittest lo considere como tal.

Para ver el reporte html, ejecutar:
        coverage html
        
'''


class Ej1Test(unittest.TestCase):
    def test_trivial(self):
        entrada = []
        salida = {}
        res = gestion_ventas(entrada)
        self.assertEqual(res, salida)

class Ej2Test(unittest.TestCase):
    def test_trivial(self):
        entrada = []
        salida = 0
        res = cantidad_digitos_impares(entrada)
        self.assertEqual(res, salida)

class Ej3Test(unittest.TestCase):
    def test_trivial(self):
        cola_entrada = Cola()
        umbral = 0 
        res = reordenar_cola_primero_numerosas(cola_entrada,umbral)
        self.assertTrue(res.empty())


class Ej4Test(unittest.TestCase):
    def test_trivial(self):
        entrada = [[1]]
        salida = True
        res = matriz_cuasi_decreciente(entrada)
        self.assertEqual(res, salida)


if __name__ == '__main__':
    unittest.main(verbosity=2)
