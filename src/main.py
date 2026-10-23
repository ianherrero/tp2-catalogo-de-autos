import re

from src.fuentes import FuenteCSV
from src.limpieza import procesar_autos
from src.analisis import (
    filtrar_por_marca,
    filtrar_por_precio_maximo,
    calcular_precio_promedio,
    buscar_modelo_regex,
)
from src.auto import Auto


def main():
    fuente = FuenteCSV("data/autos.csv")
    autos, rechazados = procesar_autos(fuente.leer())

    print("\n=== CATÁLOGO DE AUTOS USADOS ===")
    print(f"Autos disponibles: {len(autos)}")
    print(f"Registros rechazados: {rechazados}")

    if autos:
        datos = autos[0]
        auto_ejemplo = Auto(
            datos["id"],
            datos["marca"],
            datos["modelo"],
            datos["anio"],
            datos["precio_usd"],
            datos["kilometraje"],
            datos["combustible"],
            datos["transmision"],
        )
        print("\nEjemplo de auto del catálogo:")
        print(auto_ejemplo.mostrar_resumen())

    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar autos por marca")
        print("2. Buscar autos por precio máximo")
        print("3. Ver precio promedio")
        print("4. Buscar modelos con regex")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            marca = input("Ingresá una marca: ")
            resultado = filtrar_por_marca(autos, marca)

            if resultado:
                for auto in resultado:
                    print(
                        f"{auto['marca']} {auto['modelo']} ({auto['anio']}) - "
                        f"USD {auto['precio_usd']} - {auto['kilometraje']} km - {auto['combustible']} - {auto['transmision']}"
                    )
            else:
                print("No se encontraron autos de esa marca.")

        elif opcion == "2":
            try:
                precio = int(input("Ingresá el precio máximo en USD: "))
                resultado = filtrar_por_precio_maximo(autos, precio)

                if resultado:
                    for auto in resultado:
                        print(
                            f"{auto['marca']} {auto['modelo']} ({auto['anio']}) - "
                            f"USD {auto['precio_usd']} - {auto['kilometraje']} km - {auto['combustible']} - {auto['transmision']}"
                        )
                else:
                    print("No se encontraron autos en ese rango.")

            except ValueError:
                print("Error: ingresá un precio numérico.")

        elif opcion == "3":
            promedio = calcular_precio_promedio(autos)
            print(f"Precio promedio: USD {promedio:.2f}")

        elif opcion == "4":
            patron = input("Ingresá el patrón de búsqueda: ")

            try:
                resultado = buscar_modelo_regex(autos, patron)

                if resultado:
                    for auto in resultado:
                        print(
                            f"{auto['marca']} {auto['modelo']} ({auto['anio']}) - "
                            f"USD {auto['precio_usd']} - {auto['kilometraje']} km - {auto['combustible']} - {auto['transmision']}"
                        )
                else:
                    print("No se encontraron modelos.")

            except re.error:
                print("Error: la expresión regular no es válida.")

        elif opcion == "5":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida. Intentá nuevamente.")


if __name__ == "__main__":
    main()