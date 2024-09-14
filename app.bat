@echo off

REM Activa el entorno virtual
call .venv\Scripts\activate.bat

REM Ejecuta el script Python
python app.py

REM Limpia pantalla
clear
cls

REM Sale del programa
exit