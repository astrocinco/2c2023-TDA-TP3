import time
import os
import matplotlib.pyplot as plt
import backtracking as b
import setup as s

DIRECTORIO_EJEMPLO = 'C:\\Users\\Bill\\Desktop\\FIIUBA\\2C2023\\tda\\tp3\\2c2023-TDA-TP3\datos\prueba1'

def testear_carpeta(directorio):
    archivos_pruebas = os.listdir(directorio)
    tiempos = []
    cant_n = []
    for i in archivos_pruebas:
        t, n = una_ejecucion(directorio + '\\'+i)
        tiempos.append(t)
        cant_n.append(n)
    
    return tiempos, cant_n

def una_ejecucion(archivo):
    print(f"ejecutando {archivo}")
    periodistas = s.crear_diccionario_periodistas(archivo)
    n = len(periodistas.keys())
    inicio = time.time()
    b.cantidad_minima(periodistas)
    fin = time.time()

    transcurrido = fin - inicio
    n = n

    return transcurrido, n

def graficar_carpeta_vs_funcion(data : tuple):
    plt.plot(data[0], data[1], 'ro')
    plt.ylabel('some numbers')
    plt.show()
x,y = testear_carpeta(DIRECTORIO_EJEMPLO)
x =sorted(x)
y=sorted(y)
data = (x,y)
graficar_carpeta_vs_funcion(data)
print(f"tiempos: {x}, enes: {y}")