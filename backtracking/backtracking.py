import setup as s
import time

ARCHIVO_PRUEBA = "./datos/prueba1/20.txt"
N_MINIMO = 2
            
def chequear_solucion(periodistas : dict, convocados : list):   
    aux = set()
    for convocado in convocados:
        for periodista in periodistas.keys():
            if convocado in periodistas[periodista]:
                aux.add(periodista)
    
    return len(aux) == len(periodistas.keys())


def cantidad_minima(periodistas : dict):
    n_actual = len(periodistas.keys())
    n_anterior = 0
    minimo_n = 0
    ultimo_nulo = 0
    paro = 10

    while paro > 1:
        posibles = []
        hay_solucion = BT_recursivo(periodistas,posibles,n_actual)
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

    return minimo_n,convocados


######### SEGUNDA IDEA ##############

def BT_recursivo(periodistas:dict, convocados:list = [], n_minimo = 100):

    if len(periodistas.keys()) == 0: return True
    if len(convocados) == n_minimo: return False
    
    eliminados = {}
    siguiente = next(iter(periodistas.items()))
    aux = periodistas.copy()
    
    for jugador in siguiente[1]:
        convocados.append(jugador)
        for periodista in periodistas:
            if jugador in periodistas[periodista]: eliminados[periodista] = aux.pop(periodista)

        if BT_recursivo(aux, convocados, n_minimo): return True
        
        #si no es solucion, vuelvo para atras
        convocados.remove(jugador)
        devolver_periodistas(aux,eliminados)   
    return False
        
def devolver_periodistas(periodistas:dict, eliminados:dict):
    for e in eliminados.keys():
        periodistas[e] = eliminados[e]
    s.ordenar_diccionario(periodistas)
    return periodistas



### TESTING ###
    
#jugadores, periodistas = s.crear_diccionario_jugadores(ARCHIVO_PRUEBA)      
#n_minimo = cantidad_minima(jugadores, periodistas)
#convocados = llamar_BT(3,jugadores, periodistas)
#convocados = ["Barcon't", 'Armani', 'Gallardo', 'Langoni', 'El fantasma de la B', 'Soule', 'Wachoffisde Abila', 'Messi', 'Changuito Zeballos']
#print(f"cantidad minima = {n_minimo}")
#print(convocados)

#print(chequear_solucion(jugadores, periodistas, convocados))
periodistas = s.crear_diccionario_periodistas(ARCHIVO_PRUEBA)
minimo, convocados = cantidad_minima(periodistas)
#print(BT_recursivo(periodistas,convocados=convocados, n_minimo=9))
#convocados = ['Mauro Zarate', 'Gallardo', "Barcon't", 'Chiquito Romero', 'Pity Martinez', 'Beltran', 'Soule', 'Palermo','Changuito Zeballos'] 
print(chequear_solucion(periodistas,convocados))
print(f"el minimo es {minimo} y los convocados son {convocados}")
