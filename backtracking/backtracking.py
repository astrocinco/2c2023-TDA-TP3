import setup as s
ARCHIVO_PRUEBA = "./datos/datos_prueba/20.txt"
N_MINIMO = 5
#### FUNCIONES AUXILIARES #####

def remover_lista(original : list, remover):
    removidos=[]
    for f in remover:
        if f in original:
            original.pop(original.index(f))
            removidos.append(f)
    return removidos

def añadir_periodistas(original : list, añadir):
    for f in añadir:
        if not f in original:
            original.append(f)

def quitar_jugadores(jugadores : dict, jugador):
    aux = jugadores.copy()
    for j in jugadores:
        if j == jugador:
            return aux
        del aux[j]
        

def es_solucion_posible(jugadores_restantes, faltantes):
    posibles = set()
    for j in jugadores_restantes:
        for i in jugadores_restantes[j]:
            posibles.add(i)

    for f in faltantes:
        if not f in posibles:
            return False
    return True

def contiene_faltante(jugador, faltantes):
    for f in faltantes:
        if f in jugador:
            return True
    return False

            
def chequear_solucion(jugadores : dict, periodistas : list, convocados : list):   
    for j in convocados:
        for p in jugadores[j]:
            if p in periodistas:
                periodistas.remove(p)
    
    return len(periodistas) == 0

###########################################################



#### SOLUCION ####    

def llamar_BT(n : int, jugadores : dict, periodistas : list):
    aux = jugadores.copy()
    convocados = []
    for i in jugadores:
        if rec_BT(n, aux, convocados, periodistas):
            return convocados
        aux.pop(i)
    
    return convocados

def rec_BT(n : int, jugadores : dict, convocados  : list = [], faltantes : list = []):

    for jugador in jugadores:
        #no me falta cubrir ningun subconjunto, convocados será solucion
        if len(faltantes) == 0:
            return True
    
        #alcance los n convocados pero aun quedan periodistas sin satisfacer
        if len(convocados)==n:
            return False

        aux = quitar_jugadores(jugadores, jugador)

        if contiene_faltante(jugadores[jugador], faltantes) and es_solucion_posible(aux,faltantes):
            del aux[jugador] #detalle de implementacion
            convocados.append(jugador)
            removidos = remover_lista(faltantes,jugadores[jugador])
            if rec_BT(n,aux,convocados,faltantes): return True
            #Si no encuentro solución por este lado, vuelvo atrás
            añadir_periodistas(faltantes,removidos)
            convocados.pop(convocados.index(jugador))

    return False


### TESTING ###
    
jugadores, periodistas = s.crear_diccionario_jugadores(ARCHIVO_PRUEBA)      
convocados = llamar_BT(N_MINIMO,jugadores,periodistas)
#convocados = ["Barcon't", 'Armani', 'Gallardo', 'Langoni', 'El fantasma de la B', 'Soule', 'Wachoffisde Abila', 'Messi', 'Changuito Zeballos']
print(convocados)
print(chequear_solucion(jugadores, periodistas, convocados))