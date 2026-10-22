@echo off
cd /d "%~dp0"

echo Iniciando catalogo de autos...
echo.

python -m src.main

echo.
echo El programa termino o se produjo un error.
pause