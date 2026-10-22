import re

from src.fuentes import FuenteCSV
from src.limpieza import procesar_autos
from src.analisis import (
    filtrar_por_marca,
    filtrar_por_precio_maximo,
    calcular_precio_promedio,
    buscar_modelo_regex,
)


def main():
    fuente = FuenteCSV("data/autos.csv")
    autos, rechazados = procesar_autos(fuente.leer())

    print("=== CATÁLOGO DE AUTOS USADOS ===")
    print(f"Autos disponibles: {len(autos)}")
    print(f"Registros rechazados: {rechazados}")

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

            print(f"Autos encontrados: {len(resultado)}")

            for auto in resultado:
                print(auto["marca"], auto["modelo"], auto["precio_usd"])

        elif opcion == "2":
            try:
                precio = int(input("Ingresá el precio máximo en USD: "))
                resultado = filtrar_por_precio_maximo(autos, precio)

                print(f"Autos encontrados: {len(resultado)}")

                for auto in resultado:
                    print(auto["marca"], auto["modelo"], auto["precio_usd"])

            except ValueError:
                print("Error: ingresá un número válido.")

        elif opcion == "3":
            promedio = calcular_precio_promedio(autos)
            print(f"Precio promedio: USD {promedio:.2f}")

        elif opcion == "4":
            patron = input("Ingresá un patrón para buscar modelos: ")

            try:
                resultado = buscar_modelo_regex(autos, patron)

                print(f"Autos encontrados: {len(resultado)}")

                for auto in resultado:
                    print(
                        auto["marca"],
                        auto["modelo"],
                        auto["precio_usd"]
                    )

            except re.error:
                print("Error: el patrón regex no es válido.")

        elif opcion == "5":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida. Intentá nuevamente.")


if __name__ == "__main__":
    main()