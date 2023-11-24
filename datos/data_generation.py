import random
import os

def crear_subconjuntos_b(cantidad_b, cantidad_a, archivo_salida):
    listado_jugadores = open('.\listado_completo.txt','r')
    jugadores_posibles = []
    
    #creo una lista de posibles jugadores
    for linea in listado_jugadores.readlines():
        jugadores_posibles.append(linea[:-1])
    max_jugadores = len(jugadores_posibles)-1
    
    #porsi las dudas
    cantidad_a = min(cantidad_a,max_jugadores)
    
    #restrinjo aleatoriamente
    restringir = random.randint(1,7)
    if restringir == 1:
        max_posible = max_jugadores-cantidad_a
        for i in range(cantidad_b,max_posible):
            j = random.randint(0, max_jugadores-i)

    salida = open(archivo_salida, 'w')
    
    #creo los subconjuntos con los jugadores aleatorios
    for k in range(0,cantidad_b):
        subconjunto = set()
        jug = random.randint(1, cantidad_a-1)
   
        #hago que sean poco probables los subconjuntos pequeños
        if jug < 3:
            tirar_de_vuelta = random.randint(1,5)
            if tirar_de_vuelta !=1:
                while jug < 3:
                    jug = random.randint(1, cantidad_a-1)
        else:

            #hago que sean poco probables los subconjuntos muy grandes
            if jug > 6:
                if jug > 15:
                    tirar_de_vuelta = random.randint(1,20)
                else:
                    tirar_de_vuelta = random.randint(1,5)
                if tirar_de_vuelta !=1:
                    while jug > 15:
                        jug = random.randint(1, cantidad_a-1)
   
        for h in range(0,jug):
            index = random.randint(0,cantidad_a-1)
            subconjunto.add(jugadores_posibles[index]) 
        cadena = ''
        
        #escribo
        for s in subconjunto:
            cadena = s + ',' + cadena
        
        cadena = cadena[:-1]
        cadena = cadena + '\n'
        

        salida.write(cadena)

def crear_varios_data_sets(nomenclatura: str, cantidad_data, b_inicial, incremento, cantidad_a_min = 2, cantidad_a_max = 200):
    b_actual = b_inicial
    for i in range(0,cantidad_data): 
        nombre = nomenclatura + '_' + str(b_actual) + '.txt'
        crear_subconjuntos_b(b_actual, random.randint(cantidad_a_min,cantidad_a_max), nombre)
        b_actual += incremento

crear_varios_data_sets('prueba4', 50, 100, 2, 5)


