
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
        archivo = directorio +i
        aprox, subset_mayor = map_file_and_aprox_by_lp(archivo)
        aproximacion_filtrada = list(filter(lambda player: player[1] >= (1/subset_mayor), aprox))
        print(f"N aproximado {len(aproximacion_filtrada)}")
'''
def comparar_solucion_con_catedra(directory, method):
    files_results = [('5', 2), ('7', 2), ('10_pocos', 3), ('10_varios', 6),('10_todos', 10), ('15', 4), ('20', 5), ('50', 6) ,('75', 8), ('100', 9), ('200', 9)]
    for elem in files_results:
        data = map_txt(directory+elem[0]+'.txt')
'''

def comparar_solucion_con_catedra(directory, method, method_name):
    df_results = pd.DataFrame({
        'sets': ['5', '7', '10_pocos', '10_varios', '10_todos', '15', '20', '50' ,'75', '100', '200'],
        'resultados esperados': [2, 2,  3,  6, 10,  4,  5,  6 , 8,  9,  9] 
    })
    results = []
    for set in df_results['sets']:
        data = map_txt(directory+set+'.txt')

        n, players_convoked = method(data)
        results.append(n)
    df_results['resultados por ' + method_name] = results
    df_results['coincidencia'] = df_results['resultados por ' + method_name] == df_results['resultados esperados']
    return df_results

def grafico_barras():
    results = ({
     'Set': ["2000", "2500", "3000", "3500", "4000", "5000", "6000"],
     'Aproximación': [130, 295, 406, 378, 294, 199, 74],
     'b': [15, 20, 7, 11, 29, 19, 9],
     'Tiempo (s)': [0.2, 0.64, 0.69, 0.95, 1.22, 0.25, 0.06],
    })
    
    data = pd.DataFrame(results)
    
    plt.style.use('ggplot')
    data.set_index('Set').plot.bar(stacked=False)
    plt.title("Aproximaciones para sets muy grandes")
    plt.xlabel("Set")
    plt.ylabel("Número de jugadores")
    #plt.yscale('log')
    plt.show()

    return

if __name__ == "__main__":
    #ejecutar_multiples_PL("datos/sets_propios/PL/")
    grafico_barras()



"""
Datos para gráfico de ambas aproximaciones
results = ({
     'Set': ["5.txt", "20.txt", "75.txt", "200.txt", "400.txt", "1000.txt", "2500.txt", "5000.txt",],
     'Óptimo': [2, 5, 8, 9, 15, 21, 23, 27],
     'Aprox. Greedy': [2, 7, 10, 12, 23, 32, 36, 36],
     'Aprox. PL': [2, 12, 20, 27, 44, 48, 49, 49],
    })

Datos para aprox PL
     'Set': ["5.txt", "7.txt", "10p.txt", "10t.txt", "15.txt", "20.txt", "50.txt", "75.txt", "100.txt",],
     'Óptimo': [2, 2, 3, 10, 4, 5, 6, 8, 9],
     'Aproximación': [2, 2, 6, 10, 11, 12, 13, 20, 23],
     'b': [6, 6, 7, 4, 7, 7, 8, 8, 8],
     'Cota': [12, 12, 21, 40, 28, 35, 48, 64, 72],
"""