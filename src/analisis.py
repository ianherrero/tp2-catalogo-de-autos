import re
def filtrar_por_marca(autos, marca):
    resultado = []

    for auto in autos:
        if auto["marca"].lower() == marca.lower():
            resultado.append(auto)

    return resultado
def filtrar_por_precio_maximo(autos, precio_maximo):
    resultado = []

    for auto in autos:
        if auto["precio_usd"] <= precio_maximo:
            resultado.append(auto)

    return resultado

def calcular_precio_promedio(autos):
    if len(autos) == 0:
        return 0

    suma_precios = 0

    for auto in autos:
        suma_precios += auto["precio_usd"]

    promedio = suma_precios / len(autos)

    return promedio
def buscar_modelo_regex(autos, patron):
    resultado = []

    for auto in autos:
        if re.search(patron, auto["modelo"], re.IGNORECASE):
            resultado.append(auto)

    return resultado