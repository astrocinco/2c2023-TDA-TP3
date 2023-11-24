import random
import os

def crear_subconjuntos_b(cantidad_b, cantidad_a, archivo_salida):
    listado_jugadores = open('.\listado_completo.txt','r')
    jugadores_posibles = []
    
    #creo una lista de posibles jugadores
    for linea in listado_jugadores.readlines():
        jugadores_posibles.append(linea[:-1])

    #restrinjo aleatoriamente
    restringir = random.randint(1,2)
    if restringir == 1:
        for i in range(cantidad_b,45-cantidad_a):
            j = random.randint(0, 45-i)
            jugadores_posibles.pop(j)

    salida = open(archivo_salida, 'w')
    
    #creo los subconjuntos con los jugadores aleatorios
    for k in range(0,cantidad_b):
        subconjunto = set()
        jug = random.randint(0, cantidad_a-1)
   
        if jug < 3:
            if jug == 0:
                tirar_de_vuelta = 2
            else:
                tirar_de_vuelta = random.randint(1,10)
                print("tiramo de vuelta")
            if tirar_de_vuelta !=1:
                while jug < 3:
                    jug = random.randint(0, cantidad_a-1)
   
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

def crear_varios_data_sets(nomenclatura: str, cantidad_data, b_inicial, incremento):
    b_actual = b_inicial
    for i in range(0,cantidad_data): 
        nombre = nomenclatura + '_' + str(b_actual) + '.txt'
        crear_subconjuntos_b(b_actual, random.randint(1,46), nombre)
        b_actual += incremento

crear_varios_data_sets('prueba4', 30, 104, 3)


