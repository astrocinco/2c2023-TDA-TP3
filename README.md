# 2c2023-TDA-TP3
Tercer trabajo práctico de Teoría de Algoritmos 1, cátedra Buchwald-Genender. Facultad de Ingeniería de la Universidad de Buenos Aires.

Grupo compuesto por Martín González Prieto (105738), Santiago Langer (107912) y Camila Teszkiewicz (109660).

### Cómo correr programación lineal
Correr el algoritmo por programación lineal requiere instalar el paquete pulp. Ejecutar en terminal: 
> python -m pip install pulp

## Cómo probar por terminal
Para correr las soluciones por terminal debe utilizarse terminal.py. Parado sobre el directorio base del proyecto ejecutar
> python3 terminal.py ARCHIVO -TIPO

Por ejemplo para programación lineal:
> python3 terminal.py datos/sets_catedra/100.txt -lp

Para backtracking:
> python3 terminal.py datos/sets_catedra/50.txt -bt
