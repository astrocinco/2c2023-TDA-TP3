import setup as s
import time
import sys
sys.path.insert(1, '')
from datos.adt import ProblemData
from datos.data_processing import map_txt

ARCHIVO_PRUEBA = "datos/sets_catedra/200.txt"
N_MINIMO = 2
            
def chequear_solucion(periodistas : dict, convocados :set):   
    aux = set()
    for convocado in convocados:
        for periodista in periodistas.keys():
            if convocado in periodistas[periodista]:
                aux.add(periodista)
    
    return len(aux) == len(periodistas.keys())


def solution_by_backtracking(data : ProblemData):
    n_actual = len(data.B_subsets.keys())
    n_anterior = 0
    minimo_n = 0
    ultimo_nulo = 0
    paro = 2

    while paro > 1:
        #time.sleep(2)
        posibles = set()
        hay_solucion = backtracking_recursivo(data.B_subsets, posibles,n_actual)
        aux_n = n_actual

        if hay_solucion == True:
            minimo_n = n_actual
            #con el n que probó antes no habia encontrado solucion y con este sí
            if n_anterior < minimo_n: n_actual = (n_anterior+n_actual)//2  
            
            #con el anterior habia solucion y con este tambien
            else:
                if ultimo_nulo != 0: n_actual = ultimo_nulo+1
                else: n_actual = n_actual//2
            
            n_anterior = aux_n
            convocados = posibles        
            
        else:
            ultimo_nulo = n_actual
            #con el anterior no habia solucion y con este tampoco
            if minimo_n == 0 or n_anterior < minimo_n:
                if minimo_n > 0: n_actual = minimo_n - 1
                else: n_actual = n_actual * 2  
            #con el anterior habia solucion y con este no
            else: n_actual = (n_anterior+n_actual)//2         
        n_anterior = aux_n
        
        if ultimo_nulo != 0 and minimo_n != 0: paro = abs(ultimo_nulo - minimo_n)
        if ultimo_nulo == 0 and minimo_n == 1: paro = 1
 
    return minimo_n,convocados


######### SEGUNDA IDEA ##############

def backtracking_recursivo(periodistas:dict, convocados:set, n_minimo = 100):

    if len(periodistas.keys()) == 0: 
        return True
    if len(convocados) == n_minimo: 
        return False
    
    eliminados = {}
    siguiente = next(iter(periodistas.items()))
    aux = periodistas.copy()
    
    for jugador in siguiente[1]:
        convocados.add(jugador)
        for periodista in periodistas:
            if jugador in periodistas[periodista]: eliminados[periodista] = aux.pop(periodista)

        if backtracking_recursivo(aux, convocados, n_minimo): 
            return True

        #si no es solucion, vuelvo para atras
        convocados.remove(jugador)
        devolver_periodistas(aux,eliminados)   
    return False
        
def devolver_periodistas(periodistas:dict, eliminados:dict):
    periodistas.update(eliminados)
    s.ordenar_diccionario(periodistas)
    return periodistas



### TESTING ###
""" if __name__ == "__main__":
    periodistas = s.crear_diccionario_periodistas(ARCHIVO_PRUEBA)
    print(periodistas) """

if __name__ == "__main__":
    archivo = "datos/sets_propios/400.txt"
    problem_data = map_txt(archivo)
    print("Problem data:", problem_data)
    n, players_convoked = solution_by_backtracking(problem_data)
    print("Solution:", players_convoked) 
    print(f"Choosen players vs total players: {n} de {len(problem_data.A_set)}")
