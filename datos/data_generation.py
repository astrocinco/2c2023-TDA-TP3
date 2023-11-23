import random
import os

def crear_subconjuntos_b(cantidad_b, cantidad_a, archivo_salida):
    listado_jugadores = open('.\datos\listado_completo.txt','r')
    jugadores_posibles = []
    
    for linea in listado_jugadores.readlines():
        jugadores_posibles.append(linea[:-1])

    for i in range(0,cantidad_a):
        j = random.randint(0, cantidad_a-1-i)
        jugadores_posibles.pop(j)

    salida = open(archivo_salida, 'w')
    
    for k in range(0,cantidad_b):
        subconjunto = set()
        jug = random.randint(0, cantidad_a-2)
        
        for h in range(0,jug):
            index = random.randint(0,cantidad_a-1)
            subconjunto.add(jugadores_posibles[index]) 
        cadena = ''
        for s in subconjunto:
            cadena = s + ',' + cadena
        
        cadena = cadena[:-1]
        cadena = cadena + '\n'
        

        salida.write(cadena)

    


