@echo off

call %~dp0\venv\Scripts\activate

cd %~dp0

set TOKEN=5079152093:AAEVtU2FaBzKxZsM-hA3Dnhxy-SbyAUZUDM

python ytParseBot.py

pause
