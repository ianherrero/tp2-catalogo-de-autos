class Auto:
    def __init__(self, id, marca, modelo, anio, precio_usd, kilometraje,
                 combustible, transmision):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio_usd = precio_usd
        self.kilometraje = kilometraje
        self.combustible = combustible
        self.transmision = transmision

    def antiguedad(self, anio_actual=2026):
        return anio_actual - self.anio

    def es_economico(self, precio_maximo=15000):
        return self.precio_usd <= precio_maximo

    def mostrar_resumen(self):
        return (
            f"{self.marca} {self.modelo} ({self.anio}) - "
            f"USD {self.precio_usd} - {self.kilometraje} km"
        )