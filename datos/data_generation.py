import random
import os

def crear_subconjuntos_b(cantidad_b, cantidad_a, archivo_salida):
    listado_jugadores = open('.\datos\listado_completo.txt','r')
    jugadores_posibles = []
    
    for linea in listado_jugadores.readlines():
        jugadores_posibles.append(linea[:-1])

    for i in range(0,45-cantidad_a):
        j = random.randint(0, 45-i)
        jugadores_posibles.pop(j)

    salida = open(archivo_salida, 'w')
    
    for k in range(0,cantidad_b):
        subconjunto = set()
        jug = random.randint(0, cantidad_a-2)
        
        for h in range(0,jug):
            index = random.randint(0,cantidad_a-2)
            print(f"cantidad a = {cantidad_a} index = {index}, len = {len(jugadores_posibles)}")
            subconjunto.add(jugadores_posibles[index]) 
        cadena = ''
        for s in subconjunto:
            cadena = s + ',' + cadena
        
        cadena = cadena[:-1]
        cadena = cadena + '\n'
        

        salida.write(cadena)

def crear_varios_data_sets(nomenclatura: str, cantidad_data, b_inicial, incremento):
    b_actual = b_inicial
    for i in range(0,cantidad_data): 
        nombre = nomenclatura + '_' + str(b_actual) + '.txt'
        crear_subconjuntos_b(b_actual, random.randint(1,42), nombre)
        b_actual += incremento

crear_varios_data_sets('prueba1', 10, 4, 2)


