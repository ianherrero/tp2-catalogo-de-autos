# Datos del catálogo de autos usados

## 1. Procedencia de los datos

Los datos utilizados en este proyecto son ficticios y fueron generados mediante un programa en Python con fines educativos.

El catálogo contiene 50 autos usados de distintas marcas y modelos. Los precios, años y kilometrajes son simulados y no representan necesariamente valores reales del mercado.

## 2. Unidad de análisis

Cada registro representa un vehículo del catálogo.

Los datos incluyen las siguientes variables:

- id: identificador único del vehículo.
- marca: fabricante del automóvil.
- modelo: modelo del vehículo.
- anio: año de fabricación.
- precio_usd: precio ficticio en dólares estadounidenses.
- kilometraje: kilómetros recorridos.
- combustible: tipo de combustible.
- transmision: tipo de transmisión.

## 3. Generación reproducible

Los datos se generan mediante el archivo src/generar_datos.py.

Se utiliza el módulo random de Python con una semilla fija de valor 42, que permite obtener los mismos registros al ejecutar el programa nuevamente bajo las mismas condiciones.

Para generar los datos, se ejecuta desde la carpeta principal del proyecto:

python src/generar_datos.py

El programa genera 50 vehículos y guarda los mismos registros en dos archivos:

- autos.csv
- autos.json

## 4. Verificación de reproducibilidad

Para comprobar que los datos son reproducibles, se ejecutó el generador dos veces y se compararon los hashes SHA-256 de ambos archivos.

Los hashes coincidieron antes y después de ejecutar el programa, lo que confirma que los archivos conservaron exactamente el mismo contenido.

## 5. Limitaciones

Los datos son artificiales y no provienen de publicaciones reales.

Los precios no están actualizados y no deben utilizarse para tomar decisiones reales de compra o venta de vehículos.

El conjunto de datos se utiliza únicamente para practicar lectura, validación, limpieza y análisis de información con Python.