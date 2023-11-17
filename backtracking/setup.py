def crear_subconjunto(linea):
    s_aux = linea.split(",")
    ult = s_aux.pop()
    ult = ult[:-1]
    s_aux.append(ult)

    return s_aux

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
