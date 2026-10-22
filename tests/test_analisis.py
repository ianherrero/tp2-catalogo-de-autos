import unittest

from src.analisis import (
    filtrar_por_precio_maximo,
    filtrar_por_marca,
    calcular_precio_promedio,
    buscar_modelo_regex,
)
from src.auto import Auto

class TestAnalisis(unittest.TestCase):

    def test_filtrar_por_precio_maximo(self):
        autos = [
            {"modelo": "Corolla", "precio_usd": 12000},
            {"modelo": "Fiesta", "precio_usd": 18000},
            {"modelo": "Gol", "precio_usd": 15000},
        ]

        resultado = filtrar_por_precio_maximo(autos, 15000)

        self.assertEqual(len(resultado), 2)
    def test_filtrar_por_marca(self):
        autos = [
            {"marca": "Toyota"},
            {"marca": "Ford"},
            {"marca": "Toyota"},
        ]

        resultado = filtrar_por_marca(autos, "toyota")

        self.assertEqual(len(resultado), 2)

    def test_calcular_precio_promedio(self):
        autos = [
            {"precio_usd": 10000},
            {"precio_usd": 20000},
            {"precio_usd": 30000},
        ]

        resultado = calcular_precio_promedio(autos)

        self.assertEqual(resultado, 20000)

    def test_buscar_modelo_regex(self):
        autos = [
            {"modelo": "Corolla"},
            {"modelo": "Fiesta"},
            {"modelo": "Gol"},
        ]

        resultado = buscar_modelo_regex(autos, "corolla|gol")

        self.assertEqual(len(resultado), 2)
    def test_clase_auto(self):
        auto = Auto(
            "A001", "Toyota", "Corolla", 2020,
            12000, 50000, "Nafta", "Manual"
        )

        self.assertEqual(auto.antiguedad(), 6)
        self.assertTrue(auto.es_economico())
        self.assertIn("Toyota Corolla", auto.mostrar_resumen())