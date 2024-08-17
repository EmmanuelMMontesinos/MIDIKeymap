@echo off

REM Activa el entorno virtual
call .venv\Scripts\activate.bat

REM Ejecuta el script Python
python midi_keymap.py

REM Sale del programa
exit