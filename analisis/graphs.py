import matplotlib.pyplot as plt

#Grafica el tiempo de ejecución dado un dataframe (acepta que tenga más de un método)
def make_execution_time_graph(time_execution, title="Gráfico de tiempo de ejecución"):
    plt.style.use('ggplot')
    time_execution.plot()
    plt.title(title)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Tiempo [ms]")
    plt.show()
    
