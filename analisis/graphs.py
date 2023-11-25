import matplotlib.pyplot as plt
import pandas as pd

#Grafica el tiempo de ejecución dado un dataframe (acepta que tenga más de un método)
def make_execution_time_graph(time_execution, title="Gráfico de tiempo de ejecución"):
    plt.style.use('ggplot')
    time_execution.plot()
    plt.title(title)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Tiempo [ms]")
    plt.show()
    
def make_comparation_time_graph(time_a, time_b, label_a="a", label_b="b", title="Gráfico de tiempo comparativo"):
    time_comparation = pd.DataFrame()
    time_comparation[label_a] = time_a
    time_comparation[label_b] = time_b
    plt.style.use('ggplot')
    time_comparation.plot()
    plt.title(title)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Tiempo [ms]")
    plt.show()