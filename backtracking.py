import setup
import time
import sys
sys.path.insert(1, '')
from datos.adt import ProblemData
from datos.data_processing import map_txt


def chequear_solucion(periodistas : dict, convocados :set):   
    aux = set()
    for convocado in convocados:
        for periodista in periodistas.keys():
            if convocado in periodistas[periodista]:
                aux.add(periodista)
    
    return len(aux) == len(periodistas.keys())


def solution_by_backtracking(data : ProblemData):
    numero_elegidos_actual = len(data.B_subsets.keys())
    numero_elegidos_iter_anterior = 0
    minimo_numero_elegidos_valido = 0
    maximo_numero_fallido = 0
    diferencia_fallido_y_minimo_valido = 2
    dicc_ordenado = setup.ordenar_diccionario(data.B_subsets)

    while diferencia_fallido_y_minimo_valido != 1:
        posibles_convocados = set()
        hay_solucion = backtracking_recursivo(dicc_ordenado, posibles_convocados, numero_elegidos_actual)
        aux_numero_elegidos_actual = numero_elegidos_actual

        if hay_solucion:
            minimo_numero_elegidos_valido = numero_elegidos_actual
            #Con el n que probó antes no habia encontrado solucion y con este sí
            if numero_elegidos_iter_anterior < minimo_numero_elegidos_valido: 
                numero_elegidos_actual = (numero_elegidos_iter_anterior + numero_elegidos_actual) // 2  
            
            #Con el anterior habia solucion y con este tambien
            else:
                if maximo_numero_fallido != 0: 
                    numero_elegidos_actual = maximo_numero_fallido + 1
                else: 
                    numero_elegidos_actual = numero_elegidos_actual // 2
            
            numero_elegidos_iter_anterior = aux_numero_elegidos_actual
            convocados_definitivos = posibles_convocados        
            
        else:
            maximo_numero_fallido = numero_elegidos_actual
            #Con el anterior no habia solucion y con este tampoco
            if minimo_numero_elegidos_valido == 0 or numero_elegidos_iter_anterior < minimo_numero_elegidos_valido:
                if minimo_numero_elegidos_valido > 0: 
                    numero_elegidos_actual = minimo_numero_elegidos_valido - 1
                else: 
                    numero_elegidos_actual = numero_elegidos_actual * 2  
            #Con el anterior habia solucion y con este no
            else: 
                numero_elegidos_actual = (numero_elegidos_iter_anterior + numero_elegidos_actual) // 2         
        numero_elegidos_iter_anterior = aux_numero_elegidos_actual
        
        diferencia_fallido_y_minimo_valido = abs(maximo_numero_fallido - minimo_numero_elegidos_valido)
 
    return minimo_numero_elegidos_valido, convocados_definitivos


def backtracking_recursivo(periodistas:dict, convocados:set, n_minimo):
    if len(periodistas.keys()) == 0: 
        return True
    if len(convocados) == n_minimo: 
        return False
    
    eliminados = {}
    siguiente_periodista = next(iter(periodistas.items())) 
    dicc_periodistas_copia = periodistas.copy()
    
    for jugador in siguiente_periodista[1]:
        convocados.add(jugador)
        for periodista in periodistas:
            if jugador in periodistas[periodista]: 
                eliminados[periodista] = dicc_periodistas_copia.pop(periodista)

        if backtracking_recursivo(dicc_periodistas_copia, convocados, n_minimo): 
            return True

        #Si no es solucion, vuelvo para atras
        convocados.remove(jugador)
        devolver_periodistas(dicc_periodistas_copia, eliminados)   
    return False


def devolver_periodistas(periodistas:dict, eliminados:dict):
    periodistas.update(eliminados)
    setup.ordenar_diccionario(periodistas)
    return periodistas


if __name__ == "__main__":
    archivo = "datos/sets_catedra/7.txt"
    problem_data = map_txt(archivo)
    print("Problem data:", problem_data)
    n, players_convoked = solution_by_backtracking(problem_data)
    print("Solution:", players_convoked) 
    print(f"Choosen players vs total players: {n} de {len(problem_data.A_set)}")
