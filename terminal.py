import sys
sys.path.insert(1, '')
from datos.adt import ProblemData
from datos.data_processing import map_txt
from backtracking import solution_by_backtracking
from lineal_programming import solution_by_lineal_programming

def main():
    archivo_set_datos = sys.argv[1]
    solucion = sys.argv[2]

    problem_data = map_txt(archivo_set_datos)
    #print("Problem data:", problem_data)

    if solucion == "-bt":
        print("Ejecutando solución por backtracking")
        n, players_convoked = solution_by_backtracking(problem_data)

    
    elif solucion == "-lp":
        print("Ejecutando solución por programación lineal")
        n, players_convoked = solution_by_lineal_programming(problem_data)

    else:
        raise KeyError("Elija alguna de las soluciones posibles: -bt o -lp")
    
    print("Número de jugadores elegidos:", n)
    print("Jugadores elegidos:", players_convoked)
    return n, players_convoked

main()