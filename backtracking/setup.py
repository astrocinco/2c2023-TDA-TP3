def crear_subconjunto(linea):
    s_aux = linea.split(",")
    ult = s_aux.pop()
    ult = ult[:-1]
    s_aux.append(ult)
    return s_aux


def crear_diccionario_periodistas(datos):
    periodistas = {}
    archivo = open(datos,"r")
    i=0
    for linea in archivo.readlines():
        nombre = "periodista "+str(i)
        periodistas[nombre] = []
        s_aux = crear_subconjunto(linea)
        for j in s_aux:
            periodistas[nombre].append(j)
        
        i+=1
    
    return periodistas

def ordenar_diccionario(diccionario):
    diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda item: len(item[1])))
    return diccionario_ordenado

def setup_instancia_BT(datos):
    periodistas = crear_diccionario_periodistas(datos)
    return ordenar_diccionario(periodistas) 

def crear_diccionario_jugadores(datos):
    dic = {}
    periodistas = []
    archivo = open(datos,"r")
    i=0
    for linea in archivo.readlines():
        s_aux = crear_subconjunto(linea)
        nombre = "periodista "+str(i)
        periodistas.append(nombre)

        for jugador in s_aux:

            if not jugador in dic.keys():
                dic[jugador] = []
                
            dic[jugador].append(nombre)
        i+=1

    return dic, periodistas

##testing

##periodistas = setup_instancia_BT('.\datos\set_pequeño\\5.txt')
#print(periodistas)

