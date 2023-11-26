
import time
import os
import math
import timeit
import pandas as pd

import matplotlib.pyplot as plt

from datos.adt import ProblemData
from datos.data_generation import crear_problem_data
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

    cantidad_aprox = len(res_aproximacion[0])
    b = res_aproximacion[1]

    cantidad_optima = res_solucion_PLE[0]

    if b*cantidad_optima < cantidad_aprox:
        print("fallo la cota")
    else:
        print(f"Cota superior: {b*cantidad_optima} \n N aproximado : {cantidad_aprox} \n N óptimo: {cantidad_optima}") 
    
#################################################################################################################

def testear_carpeta(directorio):
    archivos_pruebas = os.listdir(directorio)
    tiempos = []
    cant_n = []
    for i in archivos_pruebas:
        t, n = una_ejecucion(directorio + '\\'+i)
        tiempos.append(t)
        cant_n.append(n)
    
    return tiempos, cant_n

def una_ejecucion(archivo):
    print(f"ejecutando {archivo}")
    periodistas = s.crear_diccionario_periodistas(archivo)
    n = len(periodistas.keys())
    inicio = time.time()
    sol = solution_by_backtracking(periodistas)
    fin = time.time()

    transcurrido = fin - inicio
    n = n
    print(f"las solucion es: {sol}, el tiempo transcurrido hasta hallar la solucion: {transcurrido}")
    return n,transcurrido

def graficar_data(data : tuple):
    
    plt.plot(data[0], data[1], 'ro')
    plt.ylabel('tiempo')
    plt.show()

def graficar_complejidad(data):
    funcion_y = crear_eje_y(data[0])
    plt.plot(data[0], funcion_y, 'bo')
    plt.ylabel('tiempo')
    plt.show()

def complejidad(x):
    return math.factorial(x)*math.log(x)

def crear_eje_y(datos):
    eje_y = []
    for d in datos:
        eje_y.append(complejidad(d))
    return eje_y

#x,y = testear_carpeta(DIRECTORIO_EJEMPLO)
#x =sorted(x)
#y=sorted(y)
#data = ([100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98],[0.13245844841003418, 121.16746163368225, 6.049673080444336, 119.30613994598389, 21.75567889213562, 249.38651776313782, 81.09268546104431, 12.758556127548218, 40.53207039833069, 174.1204354763031, 671.2161958217621, 282.330064535141, 298.9952208995819, 0.0, 0.05970573425292969, 15.471959352493286, 0.11858797073364258, 19.537774562835693, 13.98685336112976, 86.6423852443695, 23.32000160217285, 133.58351707458496, 59.701558113098145, 106.2972002029419, 171.8282458782196, 0.9339444637298584, 0.090911865234375, 5.37862229347229, 1.7449886798858643, 5.907009601593018, 2.582944869995117, 10.920216798782349, 4.411579608917236, 40.77608370780945, 4.827941417694092, 3.9928317070007324, 2.305669069290161, 15.721377611160278, 15.036562442779541, 15.199244022369385, 4.110480308532715, 17.496185064315796, 82.5553035736084, 171.67438101768494, 4.921396255493164, 242.7211263179779, 0.07531499862670898, 23.953482151031494, 72.94903588294983, 116.90357184410095])
#graficar_complejidad(data)
#print(data[0])
#print(f"tiempos: {x}, enes: {y}")