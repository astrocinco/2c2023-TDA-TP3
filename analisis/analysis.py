import sys   
import timeit
import pandas as pd

sys.path.append('aproximacion')

from aproximation import map_file_and_aprox_by_lp
#import aproximacion.aproximation as a
import prog_lineal.lineal_programming as pl
import datos.data_generation as dat

def comparar_soluciones_PL_vs_PLE(data_file):
    res_solucion_PLE = pl.map_problem_and_solve_by_PLE(data_file)
    res_aproximacion = map_file_and_aprox_by_lp(data_file)

    cantidad_aprox = len(res_aproximacion[0])
    b = res_aproximacion[1]

    cantidad_optima = res_solucion_PLE[0]

    if b*cantidad_optima < cantidad_aprox:
        print("fallo la cota")
    else:
        print(f"Cota superior: {b*cantidad_optima} \n N aproximado : {cantidad_aprox} \n N óptimo: {cantidad_optima}") 


def get_execution_time(method, max, rep, size):
    df_time = pd.DataFrame()
    for n_subsets in range(2, max):
        time = 0
        for i in range(1, rep):
            aux_set = dat.crear_problem_data(n_subsets)
            time += timeit.timeit(lambda: method(aux_set), number=size)
        time = time / rep
        
        aux_df = pd.DataFrame({"time": time*1000}, index=[n_subsets])
        df_time = pd.concat([df_time, aux_df])
    return df_time

