# Catálogo de autos usados

*Autor:* Ian Herrero  
*Materia:* Programación Orientada a Datos  
*Carrera:* Licenciatura en Ciencia de Datos – UCA  
*Trabajo:* Trabajo Práctico 2

## 1. Problema y objetivo

Al buscar un auto usado, puede resultar difícil comparar opciones cuando la información se encuentra en archivos con distintos formatos.

Este proyecto desarrolla una aplicación de consola en Python que permite cargar, validar y consultar un catálogo de autos usados.

Está dirigida a personas interesadas en comparar vehículos según su marca, modelo y precio.

## 2. Funcionalidades

El programa permite:

- Consultar autos por marca.
- Filtrar vehículos según un precio máximo en dólares.
- Calcular el precio promedio del catálogo.
- Buscar modelos mediante expresiones regulares (regex).
- Identificar y rechazar registros inválidos o duplicados.

Los resultados se muestran en la consola mediante un menú interactivo.

## 3. Datos utilizados

El catálogo contiene 50 registros ficticios generados mediante Python.

Cada fila representa un auto usado e incluye:

| Variable | Descripción |
|---|---|
| id | Identificador único del auto |
| marca | Fabricante del vehículo |
| modelo | Modelo del vehículo |
| anio | Año de fabricación |
| precio_usd | Precio expresado en dólares estadounidenses |
| kilometraje | Distancia recorrida en kilómetros |
| combustible | Tipo de combustible |
| transmision | Tipo de transmisión |

Los datos se almacenan en data/autos.csv y data/autos.json.

*Procedencia:* datos simulados mediante src/generar_datos.py, utilizando una semilla fija (42) para garantizar resultados reproducibles. No proceden de una base de datos comercial ni representan publicaciones reales.

*Condiciones de uso:* al tratarse de datos ficticios creados para este trabajo académico, no se utilizan datos personales ni fuentes externas sujetas a licencias de terceros.

## 4. Requisitos e instalación

Se necesita Python 3.

El proyecto utiliza únicamente bibliotecas estándar de Python, por lo que no requiere instalar paquetes adicionales.

## 5. Ejecución

Desde la carpeta principal del proyecto:

bash
python -m src.main


En Windows también se puede iniciar el programa haciendo doble clic sobre iniciar.bat.

Para regenerar los datos:

bash
python src/generar_datos.py


## 6. Limpieza y validación

Durante el procesamiento:

- Los valores de año, precio y kilometraje se convierten a números enteros.
- Se rechazan registros con identificador, marca o modelo vacíos.
- Se validan los años entre 1980 y 2026.
- Se rechazan precios menores o iguales a cero.
- Se rechazan kilometrajes negativos.
- Se rechazan registros con valores numéricos incorrectos.
- Se rechazan identificadores duplicados, conservando el primer registro válido.

El programa contabiliza los registros rechazados.

## 7. Diseño del programa

El proyecto separa sus responsabilidades en distintos archivos:

- src/generar_datos.py: genera los datos ficticios.
- src/fuentes.py: implementa la interfaz común FuenteDatos y las clases FuenteCSV y FuenteJSON.
- src/limpieza.py: convierte tipos, valida y procesa registros.
- src/analisis.py: implementa filtros, estadísticas y búsqueda regex.
- src/auto.py: define la clase Auto, con atributos del vehículo y métodos para calcular antigüedad, evaluar un precio máximo y mostrar un resumen.
- src/main.py: coordina la carga de datos y el menú interactivo.
- tests/: contiene las pruebas automáticas.

La expresión regular se utiliza para buscar patrones dentro de los nombres de modelos. Por ejemplo, gol|corolla busca modelos que contengan cualquiera de esos dos textos, sin distinguir mayúsculas de minúsculas.

## 8. Pruebas automáticas

Para ejecutar las pruebas:

bash
python -m unittest discover -s tests -v


Las pruebas verifican filtros, cálculos, limpieza, entradas inválidas, duplicados, funcionamiento de la clase Auto y equivalencia entre CSV y JSON.

## 9. Ejemplo de resultado

Al iniciar el programa con los datos generados, se espera obtener:

text
Autos disponibles: 50
Registros rechazados: 0


El menú permite seleccionar una operación e introducir los parámetros correspondientes.

El precio promedio representa la media aritmética de los precios de los autos válidos. No debe interpretarse como una estimación del precio promedio del mercado automotor.

## 10. Alcance y limitaciones

Esta primera versión permite consultas básicas sobre un conjunto de datos ficticios.

Sus principales limitaciones son:

- No utiliza precios reales ni actualizados del mercado.
- No incluye una interfaz gráfica.
- No permite agregar, modificar o eliminar autos desde el menú.
- La consulta principal carga los datos desde CSV.
- Las búsquedas y estadísticas dependen de los registros disponibles en el catálogo.

El proyecto tiene fines educativos y busca demostrar procesamiento reproducible de datos, programación orientada a objetos, validaciones, pruebas y control de versiones.