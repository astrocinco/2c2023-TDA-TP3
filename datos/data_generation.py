import random
import os

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
    subconjunto = set()
    jug = tamaño_aleatorio_de_b(min_tamaño_b,max_tamaño_b,cantidad_jugadores_posibles)
    
    for h in range(0,jug):
        subconjunto.add(random.choice(jugadores_posibles))
    return subconjunto

def crear_cadena_b(subconjunto_b):
    cadena = ''
    #escribo
    for s in subconjunto_b:
        cadena = s + ',' + cadena
    cadena = cadena[:-1]
    cadena = cadena + '\n'
    return cadena

def crear_subconjuntos_b(cantidad_b, cantidad_a, archivo_salida, min_tamaño_b = 1, max_tamaño_b = 0):
    listado_jugadores = open('.\listado_completo_50.txt','r')
    jugadores_posibles = []
    
    #creo una lista de posibles jugadores
    for linea in listado_jugadores.readlines():
        jugadores_posibles.append(linea[:-1])
    max_jugadores = len(jugadores_posibles)-1

    #porsi las dudas
    cantidad_a = min(cantidad_a,max_jugadores)
    
    #la restriccion del maximo de b
    if max_tamaño_b == 0:
        max_tamaño_b = max_jugadores

    #restrinjo aleatoriamente
    jugadores_posibles = recortar_aleatoriamente_los_jugadores_de_a(max_jugadores, jugadores_posibles)

    salida = open(archivo_salida, 'w')
    
    #creo los subconjuntos con los jugadores aleatorios
    for k in range(0,cantidad_b):
        subconjunto = crear_subconjunto_b(min_tamaño_b,max_tamaño_b,len(jugadores_posibles),jugadores_posibles)
        cadena = crear_cadena_b(subconjunto)
        salida.write(cadena)

def crear_varios_data_sets(nomenclatura: str, cantidad_data, b_inicial, incremento, cantidad_a_min = 2, cantidad_a_max = 200, min_tamaño_b = 1, max_tamaño_b = 0):
    b_actual = b_inicial
    for i in range(0,cantidad_data): 
        nombre = nomenclatura + '_' + str(b_actual) + '.txt'
        crear_subconjuntos_b(b_actual, random.randint(cantidad_a_min,cantidad_a_max), nombre, min_tamaño_b, max_tamaño_b)
        b_actual += incremento

crear_varios_data_sets('prueba8', 100, 50, 2, 5)


