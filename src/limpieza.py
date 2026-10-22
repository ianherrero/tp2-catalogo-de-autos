def limpiar_auto(auto):
    auto_limpio = auto.copy()

    auto_limpio["anio"] = int(auto_limpio["anio"])
    auto_limpio["precio_usd"] = int(auto_limpio["precio_usd"])
    auto_limpio["kilometraje"] = int(auto_limpio["kilometraje"])

    return auto_limpio
def validar_auto(auto):
    if not auto["id"]:
        return False

    if not auto["marca"] or not auto["modelo"]:
        return False

    if auto["anio"] < 1980 or auto["anio"] > 2026:
        return False

    if auto["precio_usd"] <= 0:
        return False

    if auto["kilometraje"] < 0:
        return False

    return True
def procesar_autos(autos):
    autos_validos = []
    autos_rechazados = 0
    ids_vistos = set()

    for auto in autos:
        try:
            auto_limpio = limpiar_auto(auto)

            if validar_auto(auto_limpio):
                if auto_limpio["id"] in ids_vistos:
                    autos_rechazados += 1
                else:
                    ids_vistos.add(auto_limpio["id"])
                    autos_validos.append(auto_limpio)
            else:
                autos_rechazados += 1

        except (ValueError, TypeError, KeyError):
            autos_rechazados += 1

    return autos_validos, autos_rechazados