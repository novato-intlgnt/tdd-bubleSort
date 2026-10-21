"""Pruebas unitarias de caja blanca: CP1–CP4 y regresiones complementarias.

Ejecutar desde la carpeta 'codigo': python -m unittest -v
"""

import unittest
from bubble_sort import Traza, bubble_sort


class TestCaminosIndependientes(unittest.TestCase):
    def verificar(self, entrada, esperado, camino, decisiones):
        datos = entrada.copy()
        traza = Traza()
        bubble_sort(datos, traza)
        self.assertEqual(datos, esperado)
        self.assertEqual(traza.nodos, camino)
        self.assertEqual(traza.decisiones, decisiones)

    def test_CP1_sin_entrar_al_bucle_externo(self):
        self.verificar(
            [7], [7],
            ["N1", "N2", "N9"],
            [("N2", "F")],
        )

    def test_CP2_comparacion_sin_intercambio(self):
        self.verificar(
            [1, 2], [1, 2],
            ["N1", "N2", "N3", "N4", "N5", "N7", "N4", "N8", "N2", "N9"],
            [("N2", "V"), ("N4", "V"), ("N5", "F"), ("N4", "F"), ("N2", "F")],
        )

    def test_CP3_comparacion_con_intercambio(self):
        self.verificar(
            [2, 1], [1, 2],
            ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N4", "N8", "N2", "N9"],
            [("N2", "V"), ("N4", "V"), ("N5", "V"), ("N4", "F"), ("N2", "F")],
        )

    def test_CP4_repeticion_de_bucles(self):
        self.verificar(
            [2, 3, 1], [1, 2, 3],
            ["N1", "N2", "N3", "N4", "N5", "N7", "N4", "N5", "N6", "N7",
             "N4", "N8", "N2", "N3", "N4", "N5", "N6", "N7", "N4", "N8",
             "N2", "N9"],
            [("N2", "V"), ("N4", "V"), ("N5", "F"), ("N4", "V"), ("N5", "V"),
             ("N4", "F"), ("N2", "V"), ("N4", "V"), ("N5", "V"), ("N4", "F"),
             ("N2", "F")],
        )


class TestRegresion(unittest.TestCase):
    def test_lista_vacia(self):
        datos = []
        bubble_sort(datos)
        self.assertEqual(datos, [])

    def test_repetidos(self):
        datos = [2, 2, 1, 1]
        bubble_sort(datos)
        self.assertEqual(datos, [1, 1, 2, 2])

    def test_valores_negativos_y_cero(self):
        datos = [0, -3, 5, -1]
        bubble_sort(datos)
        self.assertEqual(datos, [-3, -1, 0, 5])

    def test_orden_inverso(self):
        datos = [5, 4, 3, 2, 1]
        bubble_sort(datos)
        self.assertEqual(datos, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
