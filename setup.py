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
        periodistas[nombre] = set()
        s_aux = crear_subconjunto(linea)
        k = 0
        for j in s_aux:
            periodistas[nombre].add(j)
        i+=1
    
    return periodistas


def ordenar_diccionario(diccionario):
    diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda item: len(item[1])))
    return diccionario_ordenado


def setup_instancia_BT(datos):
    periodistas = crear_diccionario_periodistas(datos)
    diccionario = ordenar_diccionario(periodistas) 
    print ("Diccionario:", diccionario)
    return diccionario
