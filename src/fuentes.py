import csv
import json
from pathlib import Path


class FuenteDatos:
    def leer(self):
        raise NotImplementedError(
            "Cada fuente debe implementar el método leer()"
        )
class FuenteCSV(FuenteDatos):
    def __init__(self, ruta):
        self.ruta = Path(ruta)

    def leer(self):
        with open(self.ruta, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)

class FuenteJSON(FuenteDatos):
    def __init__(self, ruta):
        self.ruta = Path(ruta)

    def leer(self):
        with open(self.ruta, mode="r", encoding="utf-8") as archivo:
            return json.load(archivo)