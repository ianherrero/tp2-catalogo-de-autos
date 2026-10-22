
import csv
import json
import random
from pathlib import Path


# La misma semilla produce los mismos datos.
SEMILLA = 42
CANTIDAD_AUTOS = 50

DIRECTORIO_PROYECTO = Path(__file__).resolve().parent.parent
DIRECTORIO_DATOS = DIRECTORIO_PROYECTO / "data"

CAMPOS = [
    "id",
    "marca",
    "modelo",
    "anio",
    "precio_usd",
    "kilometraje",
    "combustible",
    "transmision",
]

MARCAS_MODELOS = {
    "Toyota": ["Corolla", "Etios", "Yaris"],
    "Ford": ["Focus", "Fiesta", "Ka"],
    "Volkswagen": ["Gol", "Polo", "Vento"],
    "Chevrolet": ["Onix", "Cruze", "Tracker"],
    "Peugeot": ["208", "308", "2008"],
    "Renault": ["Clio", "Sandero", "Duster"],
    "Fiat": ["Cronos", "Argo", "Palio"],
    "Honda": ["Civic", "Fit", "HR-V"],
    "Nissan": ["Versa", "Sentra", "Kicks"],
    "Citroen": ["C3", "C4", "Berlingo"],
}


def generar_autos(cantidad=CANTIDAD_AUTOS, semilla=SEMILLA):
    """Genera una lista reproducible de autos ficticios."""
    rng = random.Random(semilla)
    autos = []

    for numero in range(1, cantidad + 1):
        marca = rng.choice(list(MARCAS_MODELOS))
        modelo = rng.choice(MARCAS_MODELOS[marca])

        auto = {
            "id": f"A{numero:03d}",
            "marca": marca,
            "modelo": modelo,
            "anio": rng.randint(2010, 2025),
            "precio_usd": rng.randrange(5000, 40001, 500),
            "kilometraje": rng.randrange(0, 250001, 5000),
            "combustible": rng.choice(
                ["Nafta", "Diesel", "Híbrido"]
            ),
            "transmision": rng.choice(
                ["Manual", "Automática"]
            ),
        }

        autos.append(auto)

    return autos


def guardar_autos(autos):
    """Guarda los mismos registros en CSV y JSON."""
    DIRECTORIO_DATOS.mkdir(parents=True, exist_ok=True)

    ruta_csv = DIRECTORIO_DATOS / "autos.csv"
    ruta_json = DIRECTORIO_DATOS / "autos.json"

    with ruta_csv.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(autos)

    with ruta_json.open("w", encoding="utf-8") as archivo:
        json.dump(autos, archivo, ensure_ascii=False, indent=2)

    print(f"Se generaron {len(autos)} autos.")
    print(f"CSV: {ruta_csv}")
    print(f"JSON: {ruta_json}")


if __name__ == "__main__":
    autos = generar_autos()
    guardar_autos(autos)
