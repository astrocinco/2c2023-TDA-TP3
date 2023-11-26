import random
import os
import sys
sys.path.insert(1, '')

from datos.adt import ProblemData


def recortar_aleatoriamente_los_jugadores_de_a(max_jugadores, jugadores_posibles : list):
    restringir = random.choice([True,False,False])
    if restringir:
        cantidad_a_recortar = random.randint(1, max_jugadores-1)
        for i in range(1,cantidad_a_recortar):
            jugadores_posibles.remove(random.choice(jugadores_posibles))
    return jugadores_posibles

def tamaño_aleatorio_de_b(min_tamaño_b,max_tamaño_b, cantidad_a):
    cantidad_de_jugadores = random.randint(min_tamaño_b, max_tamaño_b)
    #hago que sean poco probables los subconjuntos pequeños
    if cantidad_de_jugadores < 3:
        tirar_de_vuelta = random.randint(1,5)
        if tirar_de_vuelta !=1:
            while cantidad_de_jugadores < 3:
                cantidad_de_jugadores = random.randint(1, cantidad_a-1)
    else:
        #hago que sean poco probables los subconjuntos muy grandes
        if cantidad_de_jugadores > 6:
            if cantidad_de_jugadores > 15:
                tirar_de_vuelta = random.randint(1,20)
            else:
                tirar_de_vuelta = random.randint(1,5)
            if tirar_de_vuelta !=1:
                while cantidad_de_jugadores > 15:
                    cantidad_de_jugadores = random.randint(1, cantidad_a-1)
    return cantidad_de_jugadores

def crear_subconjunto_b(min_tamaño_b,max_tamaño_b,cantidad_jugadores_posibles, jugadores_posibles : list):
    subconjunto = []
    jug = tamaño_aleatorio_de_b(min_tamaño_b,max_tamaño_b,cantidad_jugadores_posibles)
    
    for h in range(0,jug):
        subconjunto.append(random.choice(jugadores_posibles))
    return subconjunto

def crear_cadena_b(subconjunto_b):
    cadena = ''
    #escribo
    for s in subconjunto_b:
        cadena = s + ',' + cadena
    cadena = cadena[:-1]
    cadena = cadena + '\n'
    return cadena

def crear_problem_data(listado_jugadores_file, cantidad_de_sets, min_jugadores_por_set = 1):
    listado_jugadores = open(listado_jugadores_file,'r')
    jugadores_posibles = []
    
    #creo una lista de posibles jugadores
    for linea in listado_jugadores.readlines():
        jugadores_posibles.append(linea[:-1])
    max_jugadores = len(jugadores_posibles)-1
    
    #la restriccion del maximo de b
    max_tamaño_b = max_jugadores

    #restrinjo aleatoriamente
    jugadores_posibles = recortar_aleatoriamente_los_jugadores_de_a(max_jugadores, jugadores_posibles)
    
    all_preferences = dict()
    all_players = set()
    contador = 0
      
    #creo los subconjuntos con los jugadores aleatorios
    for k in range(0,cantidad_de_sets):
        subconjunto = crear_subconjunto_b(min_jugadores_por_set, max_tamaño_b,len(jugadores_posibles),jugadores_posibles)
        all_preferences["journalist" + str(contador)] = subconjunto
        for player in subconjunto:
            if player not in all_players:
                all_players.add(player)
        contador += 1  
    
    return ProblemData(all_players, all_preferences)


def guardar_subconjuntos_b_en_archivo(data: ProblemData, archivo_salida):
    salida = open(archivo_salida, 'w')
    for subset in data.B_subsets.values():
        cadena = crear_cadena_b(subset)
        salida.write(cadena)
    
def crear_varios_data_sets(nomenclatura: str, cantidad_data, b_inicial, incremento, cantidad_a_min = 2, cantidad_a_max = 200, min_tamaño_b = 1):
    b_actual = b_inicial
    for i in range(0,cantidad_data): 
        nombre_de_archivo = nomenclatura + '_' + str(b_actual) + '.txt'
        data = crear_problem_data(b_actual, random.randint(cantidad_a_min,cantidad_a_max), min_tamaño_b)
        guardar_subconjuntos_b_en_archivo(data, nombre_de_archivo)
        b_actual += incremento


#crear_varios_data_sets('prueba8', 100, 50, 2, 5)


