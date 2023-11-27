
import time
import os
import math
import timeit
import pandas as pd

import matplotlib.pyplot as plt

from datos.adt import ProblemData
from datos.data_generation import crear_problem_data
from datos.data_processing import map_txt
import setup as s
from backtracking import solution_by_backtracking
from aproximation import map_file_and_aprox_by_lp
from lineal_programming import map_problem_and_solve_by_PLE, solution_by_lineal_programming
from graphs import make_execution_time_graph, make_comparation_time_graph

def get_execution_time(method, min, max, rep, size):
    df_time = pd.DataFrame()
    for n_subsets in range(min, max):
        time = 0
        for i in range(1, rep):
            aux_set = crear_problem_data('datos/listado_completo_50.txt', n_subsets)
            time += timeit.timeit(lambda: method(aux_set), number=size)
        time = time / rep
        aux_df = pd.DataFrame({"time": time*1000}, index=[n_subsets])
        df_time = pd.concat([df_time, aux_df])
    return df_time

def comparar_soluciones_PL_vs_PLE(data_file):
    res_solucion_PLE = map_problem_and_solve_by_PLE(data_file)
    res_aproximacion = map_file_and_aprox_by_lp(data_file)
    
    b = res_aproximacion[1]
    aproximacion_filtrada = list(filter(lambda player: player[1] >= (1/b), res_aproximacion[0]))

    cantidad_aprox = len(aproximacion_filtrada)
    cantidad_optima = res_solucion_PLE[0]

    if b*cantidad_optima < cantidad_aprox:
        print(f"FALLO Cota superior: {b*cantidad_optima} \n N aproximado : {cantidad_aprox} \n N óptimo: {cantidad_optima}") 

    else:
        print(f"Cota superior: {b*cantidad_optima} \n N aproximado : {cantidad_aprox} \n N óptimo: {cantidad_optima}") 

def comparar_multiples_PL_vs_PLE(directorio):
    archivos_pruebas = os.listdir(directorio)
    for i in archivos_pruebas:
        print(f"archivo: {i}")
        archivo = directorio + '\\'+i
        comparar_soluciones_PL_vs_PLE(archivo)

def ejecutar_multiples_PL(directorio):
    archivos_pruebas = os.listdir(directorio)
    for i in archivos_pruebas:
        print(f"archivo: {i}")
        archivo = directorio + '\\'+i
        aprox, subset_mayor = map_file_and_aprox_by_lp(archivo)
        aproximacion_filtrada = list(filter(lambda player: player[1] >= (1/subset_mayor), aprox))
        print(f"N aproximado {len(aproximacion_filtrada)}")

def comparar_solucion_con_catedra(directory, method):
    files_results = [('5', 2), ('7', 2), ('10_pocos', 3), ('10_varios', 6),('10_todos', 10), ('15', 4), ('20', 5), ('50', 6) ,('75', 8), ('100', 9), ('200', 9)]
    for elem in files_results:
        data = map_txt(directory+elem[0]+'.txt')
        n, players_convoked = method(data)
        print("analysis.py 50 |", players_convoked)
        if(n == elem[1]):
            print(f"✔ - Se obtiene una solución optima del set con {elem[0]} subsets")
        else:
            print(f"✗ - La solución del set con {elem[0]} subsets NO es óptima")

    
ejecutar_multiples_PL("datos/sets_propios/PL")
