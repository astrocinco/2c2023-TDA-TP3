from aproximacion import aproximation as a
from prog_lineal import lineal_programming as pl
from datos.adt import ProblemData

ARCHIVO = "datos\sets_catedra\\200.txt"

def comparar_soluciones_PL_vs_PLE(data_file):
    res_solucion_PLE = pl.map_problem_and_solve_by_PLE(data_file)
    res_aproximacion = a.map_file_and_aprox_by_lp(data_file)

    cantidad_aprox = len(res_aproximacion[0])
    b = res_aproximacion[1]

    cantidad_optima = res_solucion_PLE[0]

    if b*cantidad_optima < cantidad_aprox:
        print("fallo la cota")
    else:
        print(f"Cota superior: {b*cantidad_optima} \n N aproximado : {cantidad_aprox} \n N óptimo: {cantidad_optima}") 


comparar_soluciones_PL_vs_PLE("datos\sets_catedra\\200.txt")




