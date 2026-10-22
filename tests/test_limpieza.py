import unittest

from src.limpieza import limpiar_auto, validar_auto, procesar_autos


class TestLimpieza(unittest.TestCase):

    def test_convertir_numeros(self):
        auto = {
            "id": "A001",
            "marca": "Toyota",
            "modelo": "Corolla",
            "anio": "2020",
            "precio_usd": "15000",
            "kilometraje": "65000",
        }

        resultado = limpiar_auto(auto)

        self.assertEqual(resultado["anio"], 2020)
        self.assertEqual(resultado["precio_usd"], 15000)
        self.assertEqual(resultado["kilometraje"], 65000)

    def test_rechazar_precio_negativo(self):
        auto = {
            "id": "A002",
            "marca": "Ford",
            "modelo": "Fiesta",
            "anio": 2018,
            "precio_usd": -5000,
            "kilometraje": 80000,
        }

        self.assertFalse(validar_auto(auto))

    def test_rechazar_kilometraje_negativo(self):
        auto = {
            "id": "A003",
            "marca": "Volkswagen",
            "modelo": "Gol",
            "anio": 2019,
            "precio_usd": 12000,
            "kilometraje": -100,
        }

        self.assertFalse(validar_auto(auto))

    def test_rechazar_precio_no_numerico(self):
        autos = [
            {
                "id": "A004",
                "marca": "Chevrolet",
                "modelo": "Onix",
                "anio": "2021",
                "precio_usd": "desconocido",
                "kilometraje": "30000",
            }
        ]

        validos, rechazados = procesar_autos(autos)

        self.assertEqual(len(validos), 0)
    def test_autos_duplicados(self):
        from src.limpieza import procesar_autos

        auto = {
            "id": "A001",
            "marca": "Toyota",
            "modelo": "Corolla",
            "anio": "2020",
            "precio_usd": "12000",
            "kilometraje": "50000",
            "combustible": "Nafta",
            "transmision": "Manual"
        }

        validos, rechazados = procesar_autos([auto, auto.copy()])

        self.assertEqual(len(validos), 1)
        self.assertEqual(rechazados, 1)
    def test_csv_y_json_equivalentes(self):
        from src.fuentes import FuenteCSV, FuenteJSON
        from src.limpieza import procesar_autos

        autos_csv = FuenteCSV("data/autos.csv").leer()
        autos_json = FuenteJSON("data/autos.json").leer()

        validos_csv, rechazados_csv = procesar_autos(autos_csv)
        validos_json, rechazados_json = procesar_autos(autos_json)

        self.assertEqual(validos_csv, validos_json)
        self.assertEqual(rechazados_csv, rechazados_json)
        self.assertEqual(len(validos_csv), 50)